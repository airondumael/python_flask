# Import app-based dependencies
from app import app

# Import core libraries
from lib import database

db = app.db


def add_session(_params):
    data = database.query(db.music_db, 'insert into session values(:user_id, :mida)', _params)

    return data


def remove_session(_params):
    data = database.query(db.music_db, 'delete from session where user_id = :user_id', _params)

    return data

