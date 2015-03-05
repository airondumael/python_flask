import requests
# Import root functions/objects
# Import global context
from app import app, auth
from util import utils

# Import flask dependencies
from flask import config, session, g, request
from flask import Blueprint, redirect, url_for, make_response, json

# Import core libraries here
from lib import res, database
from lib.error_handler import FailedRequest


config = app.config
db = app.db

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

    def user_exists(_user):
        data = database.get(db.music_db,
            'select user_id from users where email = "' + _user['email'] + '"', None)

        return data


    def add_user(params):
        database.query(db.music_db,
            'insert into users(`user_id`, `email`) values(:user_id, :email)', params)


    access_token = request.args.get('access_token')
    headers = {'Access-Token' : access_token}

    try:
        response = requests.get(config['FACCOUNTS_URL'] + '/user/', headers=headers)

        data = json.loads(response.text)

        if 'message' in data:
            raise FailedRequest(data['message'])


        if not user_exists(data):
            params = {
                'user_id'   : utils.generate_UUID(),
                'email'     : data['email']
            }

            add_user(params)


        return redirect('/')

    except FailedRequest, e:
        raise e
