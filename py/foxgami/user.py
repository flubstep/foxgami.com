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
                'profile_image_url': 'http://flubstep.com/images/sunglasses.jpg'
            }
        }

    @classmethod
    def get_logged_out(cls):
        return {
            'data': {
                'id': 0,
                'type': 'user'
            }
        }