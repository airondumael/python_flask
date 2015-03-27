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


# Define the blueprint: 'user', set its url prefix: app.url/user
mod_user = Blueprint('user', __name__)


# Declare all the routes

@mod_user.route('/', methods=['GET'])
@check_tokens
@make_response
def get_user(res):
    if not utils.has_scopes(request.user_id, 'user.info'):
        raise FailedRequest('You do not have permission to do this action')

    params = {
        'user_id' : request.user_id
    }

    return res.send(user.get_user(params)[0])


@mod_user.route('/all', methods=['GET'])
@check_tokens
@make_response
def get_all_users(res):
    if not utils.has_scopes(request.user_id, 'user.view_all'):
        raise FailedRequest('You do not have permission to do this action')

    result = user.get_all_users()

    if len(result) == 0:
        raise FailedRequest('No results found')

    return res.send(result)


@mod_user.route('/', methods=['POST'])
@check_tokens
@make_response
def edit_user(res):
    if not utils.has_scopes(request.user_id, 'user.info'):
        raise FailedRequest('You do not have permission to do this action')

    params = utils.get_data(app.config['USERS_FIELDS'], {}, request.values)

    if params['error']:
        raise FailedRequest(params['error'])

    params['user_id'] = request.user_id

    user.edit_user(params)
    user.edit_preference(params)

    return res.send(user.get_user(params)[0])


@mod_user.route('/<user_id>', methods=['DELETE'])
@check_tokens
@make_response
def delete_user(res, user_id):
    if not utils.has_scopes(request.user_id, 'user.delete'):
        raise FailedRequest('You do not have permission to do this action')

    params = {
        'user_id' : user_id
    }

    user.delete_user(params)

    auth.remove_scopes(params)
    auth.remove_session(params)

    return res.send('User deleted')

