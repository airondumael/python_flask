# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint

# Import app-based dependencies
from app import auth, user
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
    if not utils.has_scopes(request.headers.get('mida'), 'user.info'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    params = {
        'user_id' : request.user_id
    }

    return res.send(user.get_user(params)[0])


@mod_user.route('/', methods=['POST'])
@check_tokens
@make_response
def edit_user(res):
    if not utils.has_scopes(request.headers.get('mida'), 'user.info'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    params = {
        'user_id'   : request.user_id,
        'active'    : request.form['active'],
        'rank'      : request.form['rank']
    }
    
    user.edit_user(params)

    return res.send(user.get_user(params)[0])


@mod_user.route('/', methods=['DELETE'])
@check_tokens
@make_response
def delete_user(res):
    if not utils.has_scopes(request.headers.get('mida'), 'user.delete'):
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})

    params = {
        'user_id' : request.form['user_id']
    }

    user.delete_user(params)

    auth.remove_scopes(params)
    auth.remove_session(params)

    return res.send('User deleted')

