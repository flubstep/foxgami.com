from nose.tools import *
from .user import *

def test_user():
    name = 'dummy user'
    email = 'dummy@user.com'
    password = 'dummypass'
    profile_url = 'http://dummy.com/profile.jpg'

    user = User.create(name, email, password, profile_url)

    assert_is_not_none(user)
    assert_equal(user['name'], name)
    assert_equal(user['email'], email)
    assert_equal(user['profile_image_url'], profile_url)

    User.row_to_json(user)

    print(user)
    session_token = Session.create(user['id'])['id']
    session_obj = Session.get(session_token)
    assert_equal(session_obj['user_id'], user['id'])
