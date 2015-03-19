# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint

# Import app-based dependencies
from app import user
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
    params = {
        'user_id' : request.user_id
    }

    if utils.has_scopes(request.headers.get('mida'), 'user.info'):
        return res.send(user.get_user(params)[0])

    else:
        return res.redirect(frontend_error_url='/',
            params={'error' : 'You do not have permission to do this action'})


@mod_user.route('/', methods=['POST'])
@check_tokens
@make_response
def edit_user(res):
    params = {
        'user_id'   : request.user_id,
        'active'    : request.form['active'],
        'rank'      : request.form['rank']
    }

    user.edit_user(params)

    return res.send(params)

