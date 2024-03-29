# Import global context
from flask import current_app as app, redirect, request

# Import app-based dependencies
from util import utils

# Import core libraries
from lib import database
from lib.response import Response

# Other imports
from functools import wraps


def check_tokens(func):

    def session_expired():
        response = Response()
        response.set_header('nida', utils.nida())

        return response.redirect(frontend_error_url='/', params={'error' : 'Session expired'})


    @wraps(func)
    def wrapper(*args, **kw):
        access_token = request.headers.get('Access-Token')
        mida = request.headers.get('mida')

        if mida and access_token:
            db = database.make_engine(app.config['MYSQL_MUSIC'])

            params = {
                'mida' : mida
            }

            data = database.get(db, 'SELECT * FROM session WHERE mida = :mida', params)

            if data and utils.mida(access_token) == mida:
                request.user_id = data[0]['user_id']

                return func(*args, **kw)

            return session_expired()

        elif mida or access_token:
            return session_expired()

        else:
            return func(*args, **kw)

    return wrapper


def make_response(func):
    
    @wraps(func)
    def wrapper(*args, **kw):
        response = Response()
        response.set_header('nida', utils.nida())

        return func(res = response, *args, **kw)

    return wrapper

