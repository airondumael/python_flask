#put here all module dependedent functions to be called in the main function
from app import app
from lib import database

db = app.db

def add_user(_params):
    data = database.query(db.music_db,
        'insert into users(`user_id`, `email`) values(:user_id, :email)', _params)

    return data


def user_exists(_params):
    data = database.get(db.music_db, 'select user_id from users where email = :email', _params)

    return data

# def update():
#     params = {
#         'email'     : 'new@gmail.com',
#         'old_email' : 'sibayanjasper@gmail.com'
#     }
#     database.query(db.music_db, 'update users set email = :email where email = :old_email', params)

