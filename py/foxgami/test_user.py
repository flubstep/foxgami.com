from nose.tools import *
from .user import *
from foxgami.rdb import r, conn

def test_user():
    name = 'dummy user'
    email = 'dummy@user.com'
    password = 'dummypass'
    profile_url = 'http://dummy.com/profile.jpg'

    r.table('users').delete().run(conn)
    r.table('sessions').delete().run(conn)

    user = User.create(name, email, password, profile_url)
    user_id = user['id']

    assert_is_not_none(user)
    assert_equal(user['name'], name)
    assert_equal(user['email'], email)
    assert_equal(user['profile_image_url'], profile_url)

    # Make sure that nothing breaks on the call
    user_info = User.row_to_json(user)

    session_token = Session.create(user_id)['id']
    session_obj = Session.get(session_token)
    assert_equal(session_obj['user_id'], user_id)

    login_info = User.get_by_email_and_password(email, password)
    assert_in('id', login_info)
    assert_equal(login_info['id'], user_id)
    assert_equal(login_info['email'], user['email'])

    login_info = User.get_by_name_and_password(name, password)
    assert_in('id', login_info)
    assert_equal(login_info['id'], user_id)
    assert_equal(login_info['name'], user['name'])

    fake_login = User.get_by_email_and_password(email, 'nopassword')
    assert_equal(fake_login, None)

    # Test automatic session management
    user_info_with_session = User.row_to_json(user, with_session=True)
    session_token = user_info_with_session['extra']['session']

    session_obj = Session.get(session_token)
    assert_equal(session_obj['user_id'], user_id)