# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint

# Import app-based dependencies
from app import app, track
from util import utils

# Import core libraries
from lib.decorators import check_tokens, make_response

# Other imports
from werkzeug import secure_filename


# Define the blueprint: 'track', set its url prefix: app.url/track
mod_track = Blueprint('track', __name__)


# Declare all the routes

@mod_track.route('/<track_id>', methods=['GET'])
@check_tokens
@make_response
def get_track_info(res, track_id):
    params = {
        'track_id' : track_id
    }

    return res.send(track.get_track_info(params))


@mod_track.route('/<track_id>', methods=['POST'])
@check_tokens
@make_response
def edit_track_info(res, track_id):
    if not utils.has_scopes(request.headers.get('mida'), 'music.edit'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    params = utils.get_data(app.config['TRACKS_FIELDS'], {}, request.values)

    if params['error']:
        return res.redirect(frontend_error_url='/', params=params)

    params['track_id'] = track_id

    track.edit_track_info(params)

    return res.send(track.get_track_info(params))


@mod_track.route('/<track_id>', methods=['DELETE'])
@check_tokens
@make_response
def delete_track(res, track_id):
    if not utils.has_scopes(request.headers.get('mida'), 'music.delete'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    params = {
        'track_id' : track_id
    }

    track.delete_track(params)

    return res.send('Track deleted')


@mod_track.route('/upload', methods=['POST'])
@check_tokens
@make_response
def upload(res):
    if not utils.has_scopes(request.headers.get('mida'), 'music.add'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    messages = []

    files = request.files.getlist('file[]')

    for file in files:
        filename = secure_filename(file.filename)

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

        messages.append(message)

    return res.send(messages)

