# Import app-based dependencies
from app import app

# Import core libraries
from lib import database

db = app.db


def add_session(_params):
    data = database.query(db.music_db, 'INSERT IGNORE INTO session VALUES(:user_id, :mida)', _params)

    return data


def remove_scopes(_params):
    data = database.query(db.music_db, 'DELETE FROM user_scopes WHERE user_id = :user_id', _params)

    return data


def remove_session(_params):
    data = database.query(db.music_db, 'DELETE FROM session WHERE user_id = :user_id', _params)

    return data

