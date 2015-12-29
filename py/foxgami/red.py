from . import db

import praw
import datetime
import requests
import urllib
from datetime import tzinfo, timedelta

IMAGE_CONTENT_TYPES = {
    'image/png',
    'image/jpg',
    'image/jpeg',
    'image/gif',
}

# Include the time zone information in the datetime isoformat output
# http://stackoverflow.com/questions/19654578/python-utc-datetime-objects-iso-format-dont-include-z-zulu-or-zero-offset
class simple_utc(tzinfo):
    def tzname(self):
        return "UTC"
    def utcoffset(self, dt):
        return timedelta(0)

connection = praw.Reddit(user_agent='Foxgami v1.2')

class Comment(object):

    def __init__(self, story_id, comment_id, author='', comment='', num_children=0, submitted_at=None):
        self.story_id = story_id
        self.comment_id = comment_id
        self.author = author
        self.comment = comment
        self.num_children = num_children
        self.submitted_at = submitted_at

    def save(self):
        db.query("DELETE FROM comments WHERE comment_id = %s", [self.comment_id])
        db.query("""
            INSERT INTO comments
                (reddit_id, comment_id, comment, author, num_children, submitted_at)
            VALUES
                (%s, %s, %s, %s, %s, %s)
            """, [self.story_id, self.comment_id, self.comment, self.author, self.num_children, self.submitted_at])

    @classmethod
    def from_dict(cls, story_id, praw_comment):
        return cls(
            story_id = story_id,
            comment_id = praw_comment.id,
            author = praw_comment.author.name,
            comment = praw_comment.body,
            num_children = len(praw_comment.replies),
            submitted_at = datetime.datetime.utcfromtimestamp(praw_comment.created_utc)
            )


class Story(object):

    def __init__(self, story_id, title=None, image_url=None, submitted_at=None, comments=None):
        self.story_id = story_id
        self.title = title
        self.image_url = image_url
        self.submitted_at = submitted_at
        self.comments = comments or []

    def save(self):
        if self.image_url:
            db.query("DELETE FROM stories WHERE reddit_id = %s", [self.story_id])
            db.query("""
                INSERT INTO stories
                    (reddit_id, title, image_url, submitted_at)
                VALUES
                    (%s, %s, %s, %s)
                """,
                    [self.story_id, self.title, self.image_url, self.submitted_at]
                )
            for comment in self.comments:
                comment.save()

    @classmethod
    def from_dict(cls, praw_story):
        return cls(
            story_id = praw_story.id,
            title = praw_story.title,
            image_url = get_image_url(praw_story.url),
            submitted_at = datetime.datetime.utcfromtimestamp(praw_story.created_utc),
            comments = [
                Comment.from_dict(praw_story.id, c)
                for c in praw_story.comments
                if isinstance(c, praw.objects.Comment) and c.author and c.body
                ]
            )

    @classmethod
    def get(cls, story_id):
        story = db.query_single("""
            SELECT * FROM stories WHERE reddit_id = %s
            """, [story_id])
        comments = db.query("""
            SELECT * FROM comments WHERE reddit_id = %s
            """, [story_id])
        if story:
            return {
                'data': {
                    'id': story['reddit_id'],
                    'type': 'story',
                    'title': story['title'],
                    'image_url': story['image_url'],
                    'submitted_at': story['submitted_at'].replace(tzinfo=simple_utc()).isoformat()
                    },
                'linked': [
                    {
                        'id': comment['comment_id'],
                        'type': 'comment',
                        'user_name': comment['author'],
                        'text': comment['comment'],
                        'replies': comment['num_children'],
                        'submitted_at': comment['submitted_at'].replace(tzinfo=simple_utc()).isoformat()
                    } for comment in comments
                ]
            }
        else:
            return {
                'data': None
            }

    @classmethod
    def find(cls, subreddit='aww', limit=25, after=None):
        if after:
            # TODO: This isn't very efficient
            after_row = db.query_single("""
                SELECT submitted_at FROM stories WHERE reddit_id = %s
                """, [after])
            after_time = after_row['submitted_at']
            rows = db.query("""
                SELECT * FROM stories
                WHERE submitted_at > %s
                ORDER BY submitted_at
                DESC LIMIT %s
                """, [after_time, limit])
        else:
            rows = db.query("""
                SELECT * FROM stories
                ORDER BY submitted_at
                DESC LIMIT %s
                """, [limit])
        return [
            {
                'id': row['reddit_id'],
                'type': 'story',
                'title': row['title'],
                'image_url': row['image_url'],
                'submitted_at': row['submitted_at'].replace(tzinfo=simple_utc()).isoformat()
            } for row in rows]


def pull_latest(subreddit, after=None):
    praw_stories = connection.get_subreddit(subreddit).get_hot(limit=25)
    return [Story.from_dict(s) for s in praw_stories]


def get_image_url(url):
    r = requests.head(url)
    if r.headers.get('content-type') in IMAGE_CONTENT_TYPES:
        return url
    elif r.status_code == 200:
        return convert_page_to_image_url(url)
    else:
        return None


def convert_page_to_image_url(url):
    result = urllib.parse.urlsplit(url)
    if result.netloc == 'imgur.com':
        return get_image_url('http://i.imgur.com' + result.path + '.jpg')
    else:
        return None

