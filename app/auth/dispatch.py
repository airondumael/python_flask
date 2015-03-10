import requests
# Import root functions/objects
# Import global context
from app import app, user
from util import utils

# Import flask dependencies
from flask import config, session, g, request
from flask import Blueprint, redirect, url_for, make_response

# Import core libraries here
from lib import res, database
from lib.error_handler import FailedRequest


config = app.config

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__)


@mod_auth.route('/', methods=['GET'])
def get_freedom_auth_url():
    return (config['FACCOUNTS_URL'] + '/auth' + '?'
        + utils.encode_params(config['FACCOUNTS_PARAMS']) + '&state=admin')


# Route for auth callback
@mod_auth.route('/callback', methods=['GET'])
def freedom_callback():
    access_token = request.args.get('access_token')
    headers = {'Access-Token' : access_token}

    response = requests.get(config['FACCOUNTS_URL'] + '/user/', headers=headers)

    if response.status_code != 200:
        raise FailedRequest(response.text)


    data = response.json()
    params = {
        'user_id'   : utils.generate_UUID(),
        'email'     : data['email'],
        'role'      : 'all',
        'scope'     : 'user.info,music.list'
    }

    if not user.user_exists(params):
        user.add_user(params)
        user.add_roles(params)
        user.add_scopes(params)


    response_params = {
        'view_function' : redirect('/'),
        'trebliw'       : utils.trebliw(access_token)
    }

    return res.send(response_params)

