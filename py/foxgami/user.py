import bcrypt
from datetime import datetime
import pytz

from .rdb import r, conn

PACIFIC_TZ = pytz.timezone('US/Pacific')

def hash_password(password):
    password_bytes = password.encode('utf-8')
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt())


class Session(object):
    
    @classmethod
    def create(cls, user_id):
        session = {
            'type': 'session',
            'user_id': user_id,
            'created_at': datetime.now(PACIFIC_TZ)
        }
        results = r.table('sessions').insert(session).run(conn)
        token = results['generated_keys'][0]
        session['id'] = token
        return session

    @classmethod
    def delete(cls, token):
        r.table('sessions').filter(r.row['token'] == token).delete().run(conn)

    @classmethod
    def delete_by_user(cls, user_id):
        r.table('sessions').filter(r.row['user_id'] == user_id).delete().run(conn)

    @classmethod
    def get(cls, token):
        return r.table('sessions').get(token).run(conn)


class User(object):

    @classmethod
    def get_mock(cls):
        return {
            'data': {
                'id': 1,
                'type': 'user',
                'name': 'Albert Sheu',
                'short_name': 'Albert',
                'profile_image_url': 'http://flubstep.com/images/sunglasses.jpg'
            }
        }

    @staticmethod
    def row_to_json(row, with_session=False):
        if not row:
            return User.get_logged_out()
        user_obj = {
            'data': {
                'id': row['id'],
                'type': 'user',
                'name': row['name'],
                'short_name': row['name'].split()[0],
                'profile_image_url': row['profile_image_url']
            }
        }
        if with_session:
            session = Session.create(row['id'])
            user_obj['extra'] = { 'session': session['id'] }
        return user_obj


    @classmethod
    def create(cls, name, email, password, profile_image_url=None):
        password_hash = hash_password(password)
        user = {
            'type': 'user',
            'name': name, 
            'email': email,
            'password_hash': password_hash,
            'profile_image_url': profile_image_url,
            'created_at': datetime.now(PACIFIC_TZ)
        }
        result = r.table('users').insert(user).run(conn)
        user_id = result['generated_keys'][0]
        user['id'] = user_id
        return user

    @classmethod
    def get(cls, user_id):
        return r.table('users').get(user_id).run(conn)

    @classmethod
    def get_by_email_and_password(cls, email, password):
        password_hash = hash_password(password)
        results = r.table('users').filter(r.row['email'] == email).run(conn)
        for result in results:
            hashed = result['password_hash']
            if bcrypt.hashpw(password.encode('utf-8'), hashed) == hashed:
                return result
        else:
            return None

    @classmethod
    def get_logged_out(cls):
        return {
            'data': {
                'id': 0,
                'type': 'user'
            }
        }
