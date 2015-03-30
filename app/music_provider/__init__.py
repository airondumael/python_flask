# Import app-based dependencies
from app import app

# Import core libraries
from lib import database


db = app.db


def add_music_provider(_params):
    data = database.query(db.music_db, 'INSERT INTO music_providers VALUES(:id, :name, :description, \
        :owner_id, :image, :logo, :banner, :website, :email, :contact_numbers, :url, :date_created, NULL)', _params)

    data = database.query(db.music_db, 'UPDATE users SET role = "music_provider_owner" WHERE user_id = :owner_id', _params)

    return data


def add_music_provider_manager(_params):
    data = database.query(db.music_db, 'INSERT INTO music_provider_managers VALUES( \
        (SELECT user_id FROM users WHERE email = :email), :music_provider_id)', _params)

    data = database.query(db.music_db, 'UPDATE users SET role = "music_provider_manager" WHERE email = :email', _params)

    return data


def get_music_provider(_params):
    data = database.get(db.music_db, 'SELECT * FROM music_providers WHERE id = :id', _params)

    return data


def get_user_music_provider(_params):
    data = database.get(db.music_db, 'SELECT * FROM music_providers WHERE owner_id = :user_id', _params)

    if not data:
        data = database.get(db.music_db, 'SELECT * FROM music_providers WHERE id = \
            (SELECT music_provider_id FROM music_provider_managers WHERE user_id = :user_id)', _params)

    return data


def is_own_music_provider(_params):
    data = database.get(db.music_db, 'SELECT * FROM music_providers WHERE id = :music_provider_id AND owner_id = :user_id', _params)

    return data

