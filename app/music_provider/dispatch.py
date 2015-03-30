# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint

# Import app-based dependencies
from app import app, music_provider, user
from util import utils

# Import core libraries
from lib.decorators import check_tokens, make_response
from lib.error_handler import FailedRequest

# Other imports
import datetime


# Get config
config = app.config

# Define the blueprint: 'music_provider', set its url prefix: app.url/music-provider
mod_music_provider = Blueprint('music_provider', __name__)


# Declare all the routes

@mod_music_provider.route('/', methods=['GET'])
@check_tokens
@make_response
def get_user_music_provider(res):
    if not utils.has_scopes(request.user_id, 'music_provider.list'):
        raise FailedRequest('You do not have permission to do this action')

    params = {
        'user_id' : request.user_id
    }

    result = music_provider.get_user_music_provider(params)

    if not result:
        raise FailedRequest('No results found')

    return res.send(result)


@mod_music_provider.route('/', methods=['POST'])
@check_tokens
@make_response
def add_music_provider(res):
    if not utils.has_scopes(request.user_id, 'music_provider.add'):
        raise FailedRequest('You do not have permission to do this action')

    params = utils.get_data(['name', 'description', 'owner_id', 'image', 'logo',
        'banner', 'website', 'email', 'contact_numbers', 'url'], [], request.values)

    if params['error']:
        raise FailedRequest(params['error'])

    params['id'] = utils.generate_UUID()
    params['date_created'] = datetime.datetime.now()
    params['user_id'] = params['owner_id']
    params['scopes'] = config['SCOPES']['music_provider_owner']

    music_provider.add_music_provider(params)

    user.add_scopes(params)

    return res.send(music_provider.get_music_provider(params))


@mod_music_provider.route('/manager', methods=['POST'])
@check_tokens
@make_response
def add_music_provider_manager(res):
    if not utils.has_scopes(request.user_id, 'music_provider_manager.add'):
        raise FailedRequest('You do not have permission to do this action')

    if not request.music_provider_id:
        raise FailedRequest('Cookie music_provider_id is missing')

    params = utils.get_data(['email'], [], request.values)

    if params['error']:
        raise FailedRequest(params['error'])

    params['owner_id'] = request.user_id
    params['music_provider_id'] = request.music_provider_id
    params['scopes'] = config['SCOPES']['music_provider_manager']

    if not music_provider.is_own_music_provider(params):
        raise FailedRequest('Invalid music_provider_id')

    result = music_provider.add_music_provider_manager(params)

    if not result:
        raise FailedRequest('Invalid email')

    user.add_scopes(params)

    return res.send(params)

