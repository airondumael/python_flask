# Import flask
from flask import Flask

from flask.ext.cors import CORS

# Import core libraries
from lib import database_connection
from lib.error_handler import mod_err
from lib.database_connection import mod_db_connection


# App declaration
app = Flask(__name__, instance_relative_config = True)

# Configurations
# Adjust config based on the environment
app.config.from_pyfile('config.py')
app.config.from_pyfile('env/development.py')

CORS(app, allow_headers=app.config['ALLOWED_HEADERS'],
    origins=app.config['ALLOWED_ORIGINS'], methods=app.config['ALLOWED_METHODS'])

# Error and exception handling
app.register_blueprint(mod_err)

# DB connection
app.register_blueprint(mod_db_connection)

app.db = database_connection.get_database()

# Import blueprints
from app.auth.dispatch import mod_auth as auth_module
from app.music_provider.dispatch import mod_music_provider as music_provider_module
from app.track.dispatch import mod_track as track_module
from app.user.dispatch import mod_user as user_module

# Register imported blueprints for modules
app.register_blueprint(auth_module, url_prefix='/auth')
app.register_blueprint(music_provider_module, url_prefix='/music-provider')
app.register_blueprint(track_module, url_prefix='/track')
app.register_blueprint(user_module, url_prefix='/user')

