import sys
import json
import functools
import random
from flask import Flask, Response, request
from foxgami.red import Story
from foxgami.user import User, Session

app = Flask(__name__)


DEFAULT_PROFILE_IMAGES = [
    "http://www.foxgami.com/images/fox-portrait.png",
    "http://www.foxgami.com/images/ness-portrait.png",
    "http://www.foxgami.com/images/samus-portrait.png",
    "http://www.foxgami.com/images/peach-portrait.png",
    "http://www.foxgami.com/images/mario-portrait.png",
    "http://www.foxgami.com/images/charizard-portrait.png",
    "http://www.foxgami.com/images/pikachu-portrait.png",
    "http://www.foxgami.com/images/kirby-portrait.png",
    "http://www.foxgami.com/images/jigglypuff-portrait.png",
    "http://www.foxgami.com/images/yoshi-portrait.png",
    "http://www.foxgami.com/images/roy-portrait.png",
    "http://www.foxgami.com/images/link-portrait.png"
]


@app.after_request
def add_content_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


def return_as_json(inner_f):
    @functools.wraps(inner_f)
    def new_f(*args, **kwargs):
        result = inner_f(*args, **kwargs)
        return Response(json.dumps(
            result,
            indent=4,
            separators=(', ', ': ')
            ), mimetype='application/json')
    return new_f


@app.route('/api/stories')
@return_as_json
def get_stories():
    subreddit = request.args.get('subreddit', 'aww')
    limit = int(request.args.get('limit', 25))
    before = request.args.get('before')
    return Story.find(
        subreddit=subreddit,
        limit=limit,
        before=before
        )


@app.route('/api/stories/<string:story_id>')
@return_as_json
def get_story(story_id):
    return Story.get(story_id)


@app.route('/api/users')
@return_as_json
def get_user():
    token = request.args.get('token')
    if token:
        if token == '1234':
            return User.get_mock()
        session = Session.get(token)
        if session:
            return User.row_to_json(User.get(session['user_id']))
    return User.get_logged_out()


@app.route('/api/users', methods=['POST'])
@return_as_json
def create_user():
    user_info = request.get_json()
    user = User.create(
        name=user_info['name'],
        email=user_info['email'],
        password=user_info['password'],
        profile_image_url=random.choice(DEFAULT_PROFILE_IMAGES)
        )
    return User.row_to_json(user, with_session=True)


@app.route('/api/login', methods=['POST'])
@return_as_json
def login_user():
    login_info = request.get_json()
    user = User.get_by_email_and_password(
        email=login_info['email'],
        password=login_info['password']
        )
    return User.row_to_json(user, with_session=True)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    app.run(debug=True, port=port)
