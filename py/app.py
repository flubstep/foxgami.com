import json
import functools
from flask import Flask, Response, request
from foxgami.red import Story
from foxgami.user import User, Session

app = Flask(__name__)

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
def hardcoded_aww():
    return Story.find(25)


@app.route('/api/stories/<string:story_id>')
@return_as_json
def get_story(story_id):
    return Story.get(story_id)


@app.route('/api/users')
@return_as_json
def get_user():
    token = request.args.get('token')
    if token:
        session = Session.get(token)
        if user_id:
            return Users.get(session['user_id'])
    return User.get_logged_out()


@app.route('/api/users', methods=['POST'])
@return_as_json
def create_user():
    user_info = request.get_json()
    user_id = User.create(
        name=user_info['name'],
        email=user_info['email'],
        password=user_info['password']
        )
    return User.row_to_json(User.get(user_id), with_session=True)


@app.route('/api/login', methods=['POST'])
@return_as_json
def login_user():
    login_info = request.get_json()
    user_info = User.get_by_email_password(
        email=login_info['email'],
        password=login_info['password']
        )
    return User.row_to_json(user_info, with_session=True)


if __name__ == '__main__':
    app.run(debug=True)
