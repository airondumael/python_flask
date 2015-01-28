from flask import Response, json, config

# Write more detailed response later
def send (_data):
    _data = json.dumps(_data)
    return Response(_data, status = 200, mimetype = 'application/json')
