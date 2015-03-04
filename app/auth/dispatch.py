import requests, json
# Import root functions/objects
# Import global context
from app import app, auth
from util import utils

# Import flask dependencies
from flask import config, session, g, request
from flask import Blueprint, redirect, url_for, make_response

# Import core libraries here
from lib import res
from lib.error_handler import FailedRequest


config = app.config

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__)

# Set the route and accepted methods

# @mod_auth.route('/<query>', methods=['GET', 'POST'])
# def signin(query):
#     return res.send(auth.get_access_token(query))


@mod_auth.route('/', methods=['GET'])
def get_freedom_auth_url():
    return (config['FACCOUNTS_URL'] + '/auth' + '?'
        + utils.encode_params(config['FACCOUNTS_PARAMS']) + '&state=admin')


# Route for auth callback
@mod_auth.route('/callback', methods=['GET'])
def freedom_callback():
    data = {}
    data['access_token'] = request.args.get('access_token')
    headers = {'Access-Token' : data['access_token']}

    try:
        response = requests.get(config['FACCOUNTS_URL'] + '/user/', headers=headers)

        data['user'] = response.text

        if not data:
            raise FailedRequest('Invalid Access Token')

        return res.send(data)

    except Exception, e:
        raise FailedRequest(e)
