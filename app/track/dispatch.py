# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint

# Import app-based dependencies
from app import track

# Import core libraries
from lib.decorators import check_tokens, make_response

# Other imports
from werkzeug import secure_filename


# Define the blueprint: 'track', set its url prefix: app.url/track
mod_track = Blueprint('track', __name__)


# Declare all the routes

@mod_track.route('/upload', methods=['POST'])
@check_tokens
@make_response
def upload(res):
    messages = []

    files = request.files.getlist('file[]')

    for file in files:
        print file.filename
        filename = secure_filename(file.filename)

        message = 'Uploading ' + filename

        if file and track.allowed_file(file.filename):
            params = {
                'file'      : file,
                'filename'  : filename
            }

            track.upload_track(params)

            message += ' success'

        else:
            message += ' failed'

        messages.append(message)

    return res.send(messages)

