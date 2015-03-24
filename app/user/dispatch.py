# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint

# Import app-based dependencies
from app import app, auth, user
from util import utils

# Import core libraries
from lib.decorators import check_tokens, make_response


# Define the blueprint: 'user', set its url prefix: app.url/user
mod_user = Blueprint('user', __name__)


# Declare all the routes

@mod_user.route('/', methods=['GET'])
@check_tokens
@make_response
def get_user(res):
    if not utils.has_scopes(request.user_id, 'user.info'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    params = {
        'user_id' : request.user_id
    }

    return res.send(user.get_user(params)[0])


@mod_user.route('/all', methods=['GET'])
@check_tokens
@make_response
def get_all_users(res):
    if not utils.has_scopes(request.user_id, 'user.view_all'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    return res.send(user.get_all_users())


@mod_user.route('/', methods=['POST'])
@check_tokens
@make_response
def edit_user(res):
    if not utils.has_scopes(request.user_id, 'user.info'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    params = utils.get_data(app.config['USERS_FIELDS'], {}, request.values)

    if params['error']:
        return res.redirect(frontend_error_url='/', params={'error' : params['error']})

    params['user_id'] = request.user_id

    user.edit_user(params)
    user.edit_preference(params)

    return res.send(user.get_user(params)[0])


@mod_user.route('/<user_id>', methods=['DELETE'])
@check_tokens
@make_response
def delete_user(res, user_id):
    if not utils.has_scopes(request.user_id, 'user.delete'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    params = {
        'user_id' : user_id
    }

    user.delete_user(params)

    auth.remove_scopes(params)
    auth.remove_session(params)

    return res.send('User deleted')

