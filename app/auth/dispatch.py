# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint

# Import app-based dependencies
from app import app, auth, user
from util import utils

# Import core libraries
from lib.decorators import check_tokens, make_response
from lib.error_handler import FailedRequest

# Other imports
import requests as curl

# Get config
config = app.config

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__)


# Declare all the routes

@mod_auth.route('/', methods=['GET'])
@make_response
def get_freedom_auth_url(res):
    return res.send(config['FACCOUNTS_URL'] + '/auth' + '?' +
        utils.encode_params(config['FACCOUNTS_PARAMS']) + '&state=admin')


# Route for auth callback
@mod_auth.route('/callback', methods=['GET'])
@check_tokens
@make_response
def freedom_callback(res):
    access_token = request.args.get('access_token')
    headers = {
        'Access-Token' : access_token
    }

    response = curl.get(config['FACCOUNTS_URL'] + '/user/', headers=headers)

    if response.status_code != 200:
        raise FailedRequest(response.text)

    data = response.json()

    params = {
        'user_id'   : utils.generate_UUID(),
        'email'     : data['email'],
        'role'      : 'all',
        'scope'     : 'user.info,music.list',
        'mida'      : utils.mida(access_token)
    }

    user_data = user.user_exists(params)

    if user_data:
        params['user_id'] = user_data[0]['user_id']

    else:
        user.add_user(params)
        user.add_roles(params)
        user.add_scopes(params)

    auth.add_session(params)

    res.set_header('mida', params['mida'])

    return res.redirect('/')


# Route for auth logout
@mod_auth.route('/logout', methods=['POST'])
@check_tokens
@make_response
def logout(res):
    headers = {
        'Access-Token' : request.headers.get('access_token')
    }

    response = curl.post(config['FACCOUNTS_URL'] + '/auth/logout', headers=headers)

    params = {
        'user_id' : request.user_id
    }

    auth.remove_session(params)

    return res.redirect('/')

