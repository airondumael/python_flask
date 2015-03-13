# Import root functions/objects
# Import global context
from app import track
from flask import config, request, session, g

# Import flask dependencies
from flask import Blueprint, redirect, url_for, make_response
from lib.error_handler import FailedRequest



# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_tracks = Blueprint('track', __name__)

# Set the route and accepted methods

# @mod_auth.route('/genre', methods=['GET'])
# def get_genre(query):
#     return res.send(auth.get_access_token(query))




# @mod_auth.route('/artist', methods=['GET'])
# def get_artist(query):
#     return res.send(auth.get_access_token(query))



# @mod_auth.route('/album', methods=['GET'])
# def get_album(query):
#     return res.send(auth.get_access_token(query))