# Import app-based dependencies
from app import app

# Import core libraries
from lib import database

# Other imports
import boto


db = app.db

ALLOWED_EXTENSIONS = set(['zip', 'mp3'])
IMAGE_EXTENSIONS = set(['jpg', 'png'])

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
    data = database.query(db.music_db, 'UPDATE tracks SET title = :title, artist = :artist, \
        album = :album, album_cover = :album_cover, genre = :genre, mood = :mood, instrument = :instrument, \
        lyrics = :lyrics, country = :country WHERE track_id = :track_id', _params)

    return data


def get_recommended_tracks(_params):
    _params['genre'] = _params['genre'] if not _params['genre'] else _params['genre'].replace(',', '|')
    _params['mood'] = _params['mood'] if not _params['mood'] else _params['mood'].replace(',', '|')
    _params['instrument'] = _params['instrument'] if not _params['instrument'] else _params['instrument'].replace(',', '|')

    data = database.get(db.music_db, 'SELECT * FROM tracks WHERE genre REGEXP :genre OR \
        mood REGEXP :mood OR instrument REGEXP :instrument', _params)

    return data


def get_track_info(_params):
    data = database.get(db.music_db, 'SELECT * FROM tracks WHERE track_id = :track_id', _params)

    return data


def get_uncategorized_tracks():
    data = database.get(db.music_db, 'SELECT * FROM tracks WHERE title IS NULL OR artist IS NULL OR \
        album IS NULL OR genre IS NULL OR mood IS NULL OR instrument IS NULL ORDER BY artist, album', {})

    return data


def is_image(_filename):
    return '.' in _filename and _filename.rsplit('.', 1)[1] in IMAGE_EXTENSIONS


def search_tracks(_params):
    _params['query'] = '%' + _params['query'] + '%'
    result = {}

    data = database.get(db.music_db, 'SELECT * FROM tracks WHERE title LIKE :query', _params)
    result['title'] = data

    data = database.get(db.music_db, 'SELECT * FROM tracks WHERE artist LIKE :query', _params)
    result['artist'] = data

    data = database.get(db.music_db, 'SELECT * FROM tracks WHERE album LIKE :query', _params)
    result['album'] = data

    data = database.get(db.music_db, 'SELECT * FROM tracks WHERE genre LIKE :query', _params)
    result['genre'] = data

    return result


def upload_album_cover(_params):
    key = bucket.new_key('album_covers/' + _params['filename'])

    key.set_contents_from_file(_params['file'], policy='public-read')


def upload_track(_params):
    key = bucket.new_key(_params['filename'])

    key.set_contents_from_file(_params['file'], policy='public-read')

