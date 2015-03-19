# Import app-based dependencies
from app import app

# Import core libraries
from lib import database

db = app.db


def add_roles(_params):
    data = database.query(db.music_db, 'INSERT INTO user_roles VALUES(:user_id, :role)', _params)

    return data


def add_user(_params):
    data = database.query(db.music_db, 'INSERT INTO users(`user_id`, `email`) VALUES(:user_id, :email)', _params)

    return data


def edit_user(_params):
    data = database.query(db.music_db, 'UPDATE users SET active = :active, rank = :rank WHERE user_id = :user_id', _params)

    return data


def get_user(_params):
    data = database.get(db.music_db, 'SELECT * FROM users WHERE user_id = :user_id', _params)

    return data


def user_exists(_params):
    data = database.get(db.music_db, 'SELECT * FROM users WHERE email = :email', _params)

    return data


def get_scopes(_params):
    data = database.get(db.music_db, 'SELECT scope FROM scopes WHERE roles LIKE \
        CONCAT(CONCAT("%", (SELECT role FROM user_roles WHERE user_id = :user_id)), "%");', _params)

    return data

