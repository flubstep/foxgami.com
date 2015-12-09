import json
import functools
from flask import Flask, Response
from foxgami.red import Story, Story
from foxgami.user import Users

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
    return Users.get_current()


if __name__ == '__main__':
    app.run(debug=True)
