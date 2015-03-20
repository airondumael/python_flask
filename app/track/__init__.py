# Import app-based dependencies
from app import app

# Import core libraries
from lib import database

# Other imports
import boto


db = app.db

ALLOWED_EXTENSIONS = set(['zip', 'mp3'])

s3 = boto.connect_s3()
bucket = s3.get_bucket('music.tm')


def add_track(_params):
    data = database.query(db.music_db, 'INSERT INTO tracks(`track_id`, `filename`) VALUES(:track_id, :filename)', _params)

    return data


def allowed_file(_filename):
    return '.' in _filename and _filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def delete_track(_params):
    data = database.query(db.music_db, 'DELETE FROM tracks WHERE track_id = :track_id', _params)

    return data


def edit_track_info(_params):
    data = database.query(db.music_db, 'UPDATE tracks SET title = :title, artist = :artist, album = :album, genre = :genre, \
        mood = :mood, instrument = :instrument, lyrics = :lyrics, country = :country WHERE track_id = :track_id', _params)

    return data


def get_track_info(_params):
    data = database.get(db.music_db, 'SELECT * FROM tracks WHERE track_id = :track_id', _params)

    return data


def upload_track (_params):
    key = bucket.new_key(_params['filename'])

    key.set_contents_from_file(_params['file'], policy='public-read')

