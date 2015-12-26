from . import db

import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())


class Session(object):
    
    @classmethod
    def create(cls, user_id):
        new_token = str(uuid.uuid4())
        db.query('''
            INSERT INTO sessions (user_id, token)
            VALUES (%s, %s)
            ''', (user_id, new_token))
        return token

    @classmethod
    def delete(cls, token):
        db.query('''
            DELETE FROM sessions WHERE token = %s
            ''', (token,))

    @classmethod
    def delete_by_user(cls, user_id):
        db.query('''
            DELETE FROM sessions WHERE user_id = %s
            ''', (user_id,))

    @classmethod
    def get(cls, token):
        return db.query_single('''
            SELECT user_id FROM sessions WHERE token = %s
            ''', (token,))


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
    def row_to_json(row):
        if not row:
            return None
        return {
            'data': {
                'id': row['user_id'],
                'type': 'user',
                'name': row['name'],
                'short_name': row['name'].split()[0],
                'profile_image_url': row['profile_image_url']
            }
        }

    @classmethod
    def create(cls, name, email, password, profile_image_url=None):
        password_hash = hash_password(password)
        user_id = db.query('''
            INSERT INTO users
                (name, email, password_hash, profile_image_url)
            VALUES
                (%s, %s, %s, %s)
            ''', (name, email, password_hash, profile_image_url)
            )
        return user_id

    @classmethod
    def get(cls, user_id):
        return db.query('''
            SELECT * FROM users
            WHERE user_id = %s
            ''', (user_id))

    @classmethod
    def get_logged_out(cls):
        return {
            'data': {
                'id': 0,
                'type': 'user'
            }
        }