# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint

# Import app-based dependencies
from app import app, music_provider
from util import utils

# Import core libraries
from lib.decorators import check_tokens, make_response


# Define the blueprint: 'music_provider', set its url prefix: app.url/music-provider
mod_music_provider = Blueprint('music_provider', __name__)


# Declare all the routes

@mod_music_provider.route('/', methods=['POST'])
@check_tokens
@make_response
def add_music_provider(res):
    if not utils.has_scopes(request.user_id, 'music_provider.add'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    params = utils.get_data(app.config['MUSIC_PROVIDERS_FIELDS'], {}, request.values)

    if params['error']:
        return res.redirect(frontend_error_url='/', params=params)

    params['id'] = utils.generate_UUID()

    music_provider.add_music_provider(params)

    return res.send(params)

