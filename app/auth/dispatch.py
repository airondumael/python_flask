# Import root functions/objects
# Import global context
from app import auth
from flask import config, request, session, g

# Import flask dependencies
from flask import Blueprint, redirect, url_for, make_response
from lib import res
from lib.error_handler import FailedRequest



# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__)

# Set the route and accepted methods

@mod_auth.route('/', methods=['GET', 'POST'])
def signin():
    return res.send(auth.get_access_token('string'))
