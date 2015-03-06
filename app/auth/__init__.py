#put here all module dependedent functions to be called in the main function
from app import app
from lib import database

config = app.config
db = app.db

def get_access_token (_data):
    
    params = {
        'id' : _data,
        'test': "tessst333"
    }

    # data = db.earnings_db.execute("select * from report where id = 12345", params)
    # # print data.keys()
    # for row in data:
    #     for col, val in row.items():
    #         print col + ': ' + val

    data = database.query(db.earnings_db, 'insert into temp values(:id, :test)', params)
    # data = database.get(db.earnings_db, 'select * from report', (), False)

    return data


# Accepts {'username': '', 'password': ''} data format
# Returns user_data or error message
def check_login (_data):
    if 'username' in _data and 'password' in _data:
        return True


def add_user(_params):
        data = database.query(db.music_db,
            'insert into users(`user_id`, `email`) values(:user_id, :email)', _params)

        return data


def user_exists(_user):
        data = database.get(db.music_db,
            'select user_id from users where email = "' + _user['email'] + '"', None)

        return data
