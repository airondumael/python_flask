# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint

# Import app-based dependencies
from app import app, track, user
from util import utils

# Import core libraries
from lib.decorators import check_tokens, make_response
from lib.error_handler import FailedRequest

# Other imports
from werkzeug import secure_filename
import datetime


# Get config
config = app.config

# Define the blueprint: 'track', set its url prefix: app.url/track
mod_track = Blueprint('track', __name__)


# Declare all the routes

@mod_track.route('/<track_id>', methods=['GET'])
@check_tokens
@make_response
def get_track_info(res, track_id):
    if not utils.has_scopes(request.user_id, 'music.list'):
        raise FailedRequest('You do not have permission to do this action')

    params = {
        'track_id' : track_id
    }

    result = track.get_track_info(params)

    if not result:
        raise FailedRequest('Invalid track_id')

    return res.send(result)


@mod_track.route('/<track_id>', methods=['POST'])
@check_tokens
@make_response
def edit_track_info(res, track_id):
    if not utils.has_scopes(request.user_id, 'music.meta'):
        raise FailedRequest('You do not have permission to do this action')

    params = utils.get_data(['title', 'artist', 'album', 'album_cover',
        'genre', 'mood', 'instrument', 'lyrics', 'country'], [], request.values)

    if params['error']:
        raise FailedRequest(params['error'])

    params['track_id'] = track_id

    album_cover = request.files.get('image')

    if album_cover and track.is_image(album_cover.filename):
        upload_params = {
            'image'             : album_cover,
            'image_filename'    : secure_filename(album_cover.filename)
        }
        params['album_cover'] = config['S3_URL'] + '/album_covers/' + upload_params['image_filename']

        track.upload_album_cover(upload_params)

    track.edit_track_info(params)

    result = track.get_track_info(params)

    if not result:
        raise FailedRequest('Invalid track_id')

    return res.send(result)


@mod_track.route('/<track_id>', methods=['DELETE'])
@check_tokens
@make_response
def delete_track(res, track_id):
    if not utils.has_scopes(request.user_id, 'music.delete'):
        raise FailedRequest('You do not have permission to do this action')

    params = {
        'track_id' : track_id
    }

    result = track.delete_track(params)

    if not result:
        raise FailedRequest('Invalid track_id')

    return res.send('Track deleted')


# @mod_track.route('/download/<track_id>', methods=['GET'])
# @check_tokens
# @make_response
# def download_track(res, track_id):
#     params = {
#         'track_id' : track_id
#     }

#     result = track.get_track_info(params)

#     if not result:
#         raise FailedRequest('Invalid track_id')

#     return res.send('s3.amazonaws.com/music.tm/' + result[0]['filename'])


@mod_track.route('/recommended', methods=['GET'])
@check_tokens
@make_response
def get_recommended_tracks(res):
    if not utils.has_scopes(request.user_id, 'music.list', 'user.info'):
        raise FailedRequest('You do not have permission to do this action')

    params = {
        'user_id' : request.user_id
    }

    data = user.get_preference(params)[0]

    params = {
        'genre'         : data['genre'],
        'mood'          : data['mood'],
        'instrument'    : data['instrument']
    }

    result = track.get_recommended_tracks(params)

    if not result:
        raise FailedRequest('No results found')

    return res.send(result)


@mod_track.route('/search', methods=['GET'])
@mod_track.route('/search/<query>', methods=['GET'])
# @check_tokens
@make_response
def search_tracks(res, query=None):
    # if not utils.has_scopes(request.user_id, 'music.list'):
    #     raise FailedRequest('You do not have permission to do this action')

    if not query:
        raise FailedRequest('No results found')

    params = {
        'query' : query
    }

    return res.send(track.search_tracks(params))


@mod_track.route('/uncategorized', methods=['GET'])
@check_tokens
@make_response
def get_uncategorized_tracks(res):
    if not utils.has_scopes(request.user_id, 'music.meta', 'music.list'):
        raise FailedRequest('You do not have permission to do this action')

    result = track.get_uncategorized_tracks()

    if not result:
        raise FailedRequest('No results found')

    return res.send(result)


@mod_track.route('/upload', methods=['POST'])
@check_tokens
@make_response
def upload_track(res):
    if not utils.has_scopes(request.user_id, 'music.add', 'music.meta'):
        raise FailedRequest('You do not have permission to do this action')

    params = utils.get_data(['title', 'artist', 'album', 'genre',
        'mood', 'instrument', 'lyrics', 'country'], [], request.values)

    if params['error']:
            raise FailedRequest(params['error'])

    file = request.files.get('track')

    if not file:
        raise FailedRequest('track is missing or no selected file')

    filename = secure_filename(file.filename)

    if not track.allowed_file(file.filename):
        raise FailedRequest('File not allowed')

    params['track_id'] = utils.generate_UUID()
    params['album_cover'] = None
    params['filename'] = filename
    params['s3_filename'] = track.generate_filename(filename)
    params['date_created'] = datetime.datetime.now()
    params['track'] = file

    album_cover = request.files.get('image')

    if not album_cover:
        params['message'] = 'No album cover'

    elif track.is_image(album_cover.filename):
        upload_params = {
            'image'             : album_cover,
            'image_filename'    : secure_filename(album_cover.filename)
        }
        params['album_cover'] = config['S3_URL'] + '/album_covers/' + upload_params['image_filename']

        track.upload_album_cover(upload_params)

    else:
        params['message'] = 'Album cover not allowed'

    # Disable upload to S3 for now
    # TODO: Run upload in background
    # track.upload_track(params)

    track.add_track(params)

    params.pop('track', None)

    return res.send(params)

