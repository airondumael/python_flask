# Import app-based dependencies
from app import app

# Import core libraries
from lib import database

db = app.db

def add_roles(_params):
    data = database.query(db.music_db, 'insert into user_roles values(:user_id, :role)', _params)

    return data


def add_scopes(_params):
    data = database.query(db.music_db, 'insert into user_scopes values(:user_id, :scope)', _params)

    return data


def add_session(_params):
    data = database.query(db.music_db, 'insert into session values(:user_id, :mida)', _params)

    return data


def add_user(_params):
    data = database.query(db.music_db,
        'insert into users(`user_id`, `email`) values(:user_id, :email)', _params)

    return data


def user_exists(_params):
    data = database.get(db.music_db, 'select user_id from users where email = :email', _params)

    return data


# def update_user(_params):
#     data = database.query(db.music_db, 'update users set email = :email where email = :old_email', _params)

#     return data


# def delete_user(_params):
#     data = database.query(db.music_db, 'delete from users where email = :email', _params)

#     return data

