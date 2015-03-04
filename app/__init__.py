# Import flask
from flask import Flask, jsonify

# Import core libraries here
from lib import database
from lib.error_handler import mod_err

# App declaration
app = Flask(__name__, instance_relative_config = True)

# Configurations
# Adjust config based on the environment
app.config.from_pyfile('config.py')
app.config.from_pyfile('env/development.py')

# Error and exception handling
app.register_blueprint(mod_err)


# Database connections declaration
# TODO: Generalize adding of db engines
earnings_db = database.make_engine(app.config['MYSQL_EARNINGS'])

@app.teardown_appcontext
def shutdown_session(exception=None):
    """Remove the local session after executing the request."""
    earnings_db.remove()

# ===================END DB======================== #

# Import blueprints here
from app.auth.dispatch import mod_auth as auth_module

# Register imported blueprints for modules
app.register_blueprint(auth_module, url_prefix='/auth')
