from flask import Response, json, config

# Write more detailed response later
def send (_data):
    _data = json.dumps(_data)
    return Response(_data, status = 200, mimetype = 'application/json')

class FailedRequest(Exception):
    status_code = 404

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
