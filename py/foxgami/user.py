from . import db

class Users(object):

    @classmethod
    def get_current(cls):
        return {
            'data': {
                'id': 1,
                'type': 'user',
                'name': 'Albert Sheu',
                'short_name': 'Albert',
                'profile_image_url': 'https://google.com'
            }
        }