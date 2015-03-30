# Import app-based dependencies
from app import app

# Import core libraries
from lib import database


db = app.db


def add_preference(_params):
    data = database.query(db.music_db, 'INSERT INTO user_preferences(`user_id`) VALUES(:user_id)', _params)

    return data


def add_scopes(_params):
    if not _params['user_id']:
        data = database.get(db.music_db, 'SELECT user_id FROM users WHERE email = :email', _params)

        if not data:
            return data

        _params['user_id'] = data[0]['user_id']

    query = 'INSERT IGNORE INTO user_scopes VALUES '

    for scope in _params['scopes']:
        query += '(:user_id, \'' + scope + '\'),'

    data = database.query(db.music_db, query[:-1], _params)

    return data


def add_user(_params):
    data = database.query(db.music_db, 'INSERT INTO users(`user_id`, `email`, `role`) VALUES(:user_id, :email, :role)', _params)

    return data


def delete_user(_params):
    data = database.query(db.music_db, 'UPDATE users SET active = 0 WHERE user_id = :user_id', _params)

    return data


def edit_preference(_params):
    _params['genre'] = None if _params['genre'] == '' else _params['genre']
    _params['mood'] = None if _params['mood'] == '' else _params['mood']
    _params['instrument'] = None if _params['instrument'] == '' else _params['instrument']

    data = database.query(db.music_db, 'UPDATE user_preferences SET genre = :genre, \
        mood = :mood, instrument = :instrument WHERE user_id = :user_id', _params)

    return data


def edit_user(_params):
    data = database.query(db.music_db, 'UPDATE users SET active = :active, rank = :rank WHERE user_id = :user_id', _params)

    return data


def get_all_users(_params):
    _params['start'] = (_params['page'] - 1) * _params['entries']

    data = database.get(db.music_db, 'SELECT * FROM users LIMIT :start, :entries', _params)

    return data


def get_preference(_params):
    data = database.get(db.music_db, 'SELECT * FROM user_preferences WHERE user_id = :user_id', _params)

    return data


def get_user(_params):
    data = database.get(db.music_db, 'SELECT users.*, genre, mood, instrument FROM users \
        JOIN user_preferences WHERE users.user_id = :user_id', _params)

    return data


def user_exists(_params):
    data = database.get(db.music_db, 'SELECT * FROM users WHERE email = :email', _params)

    return data


# def get_scopes(_params):
#     data = database.get(db.music_db, 'SELECT scope FROM scopes WHERE roles LIKE \
#         CONCAT(CONCAT("%", (SELECT role FROM user_roles WHERE user_id = :user_id)), "%");', _params)

#     return data

