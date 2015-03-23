# Import global context
from flask import json, make_response, redirect

# Import app-based dependencies
from util import utils


class Response():

    def __init__(self):
        self.headers = {}


    def set_header(self, key, value):
        self.headers[key] = value


    def send(self, data):
        response = make_response(json.dumps(data))

        # set this later in config
        response.mimetype = 'application/json'

        response.status = '200'

        for key in self.headers:
            response.headers.add(key, self.headers[key])

        return response


    def redirect(self, frontend_url=None, frontend_error_url=None, params={}):
        if frontend_url:
            response = make_response(redirect(frontend_url + '?' + utils.encode_params(params)))

        else:
            response = make_response(redirect(frontend_error_url + '?' + utils.encode_params(params)))

        return response

