from util import utils

from flask import Response, json, make_response

# Write more detailed response later
# def send (_data):
#     _data = json.dumps(_data)
#     return Response(_data, status = 200, mimetype = 'application/json')


def send(_data):
    if type(_data) == dict:
        response = make_response(_data['view_function'])

        if _data['trebliw']:
            response.set_cookie('trebliw', _data['trebliw'])

    else:
        response = Response(json.dumps(_data), status=200, mimetype='application/json')


    response.set_cookie('nida', utils.nida())

    return response

