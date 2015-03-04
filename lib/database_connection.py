# Import flask
from flask import Blueprint

from instance.env import development

# Import core libraries here 
from lib import database


class Database():

    def __init__(self):
        self.engines = []

    def add_engine(self, config):
        engine = database.make_engine(config)
        self.engines.append(engine)
        return engine

# Blueprint declaration
mod_db_connection = Blueprint('mod_db_connection', __name__)

db = Database()

# Database connections declaration
db.earnings_db = db.add_engine(development.MYSQL_EARNINGS)

@mod_db_connection.teardown_app_request
def shutdown_session(exception=None):
    """Remove the local session after executing the request."""
    for engine in db.engines:
        engine.remove()

# ===================END DB======================== #

def get_database():
    return db
