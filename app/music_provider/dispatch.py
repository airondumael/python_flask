# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint

# Import app-based dependencies
from app import app, music_provider, user
from util import utils

# Import core libraries
from lib.decorators import check_tokens, make_response

# Other imports
import datetime


# Define the blueprint: 'music_provider', set its url prefix: app.url/music-provider
mod_music_provider = Blueprint('music_provider', __name__)


# Declare all the routes

@mod_music_provider.route('/', methods=['GET'])
@check_tokens
@make_response
def get_user_music_providers(res):
    if not utils.has_scopes(request.user_id, 'music_provider.list'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    params = {
        'user_id' : request.user_id
    }

    return res.send(music_provider.get_user_music_providers(params))


@mod_music_provider.route('/', methods=['POST'])
@check_tokens
@make_response
def add_music_provider(res):
    if not utils.has_scopes(request.user_id, 'music_provider.add'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    params = utils.get_data(app.config['MUSIC_PROVIDERS_FIELDS'], {}, request.values)

    if params['error']:
        return res.send({'error' : params['error']})

    params['id'] = utils.generate_UUID()
    params['date_created'] = datetime.datetime.now()
    params['user_id'] = params['owner_id']
    params['scopes'] = ['music_provider.list', 'music_provider_manager.add']

    music_provider.add_music_provider(params)

    user.add_scopes(params)

    return res.send(music_provider.get_music_provider(params))


@mod_music_provider.route('/manager', methods=['POST'])
@check_tokens
@make_response
def add_music_provider_manager(res):
    if not utils.has_scopes(request.user_id, 'music_provider_manager.add'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    params = utils.get_data(['email', 'music_provider_id'], {}, request.values)

    if params['error']:
        return res.send({'error' : params['error']})

    params['user_id'] = request.user_id

    if music_provider.is_own_music_provider(params):
        music_provider.add_music_provider_manager(params)

    return res.send(params)

