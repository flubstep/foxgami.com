from . import db

import praw
import datetime
import requests
import urllib

IMAGE_CONTENT_TYPES = {
    'image/png',
    'image/jpg',
    'image/jpeg',
    'image/gif',
}

connection = praw.Reddit(user_agent='Foxgami v1.2')

class Story(object):

    def __init__(self, story_id, title=None, image_url=None, submitted_at=None):
        self.story_id = story_id
        self.title = title
        self.image_url = image_url
        self.submitted_at = submitted_at

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
        else:
            pass

    def update_comments(self):
        pass

    @classmethod
    def from_dict(cls, praw_story):
        return cls(
            story_id = praw_story.id,
            title = praw_story.title,
            image_url = get_image_url(praw_story.url),
            submitted_at = datetime.datetime.utcfromtimestamp(praw_story.created)
            )

    @classmethod
    def find(cls, number=10):
        rows = db.query("""
            SELECT * FROM stories
            ORDER BY submitted_at
            DESC LIMIT %s
            """, [number])
        return [
            {
                'id': row['reddit_id'],
                'title': row['title'],
                'image_url': row['image_url'],
                'submitted_at': row['submitted_at'].isoformat()
            } for row in rows]


def pull_latest(subreddit, after=None):
    praw_stories = connection.get_subreddit(subreddit).get_hot(limit=10)
    return [Story.from_dict(s) for s in praw_stories]


def get_image_url(url):
    r = requests.head(url)
    if r.headers['content-type'] in IMAGE_CONTENT_TYPES:
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

