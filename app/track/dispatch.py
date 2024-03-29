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

    return res.send(track.get_track_info(params)[0])


@mod_track.route('/<track_id>', methods=['POST'])
@check_tokens
@make_response
def edit_track_info(res, track_id):
    if not utils.has_scopes(request.user_id, 'music.meta'):
        raise FailedRequest('You do not have permission to do this action')

    params = utils.get_data(app.config['TRACKS_FIELDS'], {}, request.values)

    if params['error']:
        raise FailedRequest(params['error'])

    params['track_id'] = track_id

    track.edit_track_info(params)

    return res.send(track.get_track_info(params)[0])


@mod_track.route('/<track_id>', methods=['DELETE'])
@check_tokens
@make_response
def delete_track(res, track_id):
    if not utils.has_scopes(request.user_id, 'music.delete'):
        raise FailedRequest('You do not have permission to do this action')

    params = {
        'track_id' : track_id
    }

    track.delete_track(params)

    return res.send('Track deleted')


# @mod_track.route('/download/<track_id>', methods=['GET'])
# @check_tokens
# @make_response
# def download_track(res, track_id):
#     params = {
#         'track_id' : track_id
#     }

#     data = track.get_track_info(params)

#     if not data:
#         raise FailedRequest(params['error'])

#     return res.send('s3.amazonaws.com/music.tm/' + data[0]['filename'])


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

    return res.send(track.get_recommended_tracks(params))


@mod_track.route('/search', methods=['GET'])
def search():
    raise FailedRequest('The Monkey Ninja cannot find your request')


@mod_track.route('/search/<query>', methods=['GET'])
# @check_tokens
@make_response
def search_tracks(res, query):
    # if not utils.has_scopes(request.user_id, 'music.list'):
    #     raise FailedRequest('You do not have permission to do this action')

    params = {
        'query' : query
    }

    return res.send(track.search_tracks(params))


@mod_track.route('/upload', methods=['POST'])
@check_tokens
@make_response
def upload_track(res):
    if not utils.has_scopes(request.user_id, 'music.add'):
        raise FailedRequest('You do not have permission to do this action')

    result = []

    files = request.files.getlist('file[]')

    for file in files:
        filename = secure_filename(file.filename)

        params = {}
        message = 'Uploading ' + filename

        if file and track.allowed_file(file.filename):
            params = {
                'track_id'  : utils.generate_UUID(),
                'file'      : file,
                'filename'  : filename
            }

            track.upload_track(params)
            track.add_track(params)

            message += ' success'

        else:
            message += ' failed'

        params.pop('file', None)
        params['message'] = message

        result.append(params)

    return res.send(result)

