# Other imports
import boto


ALLOWED_EXTENSIONS = set(['zip', 'mp3'])

s3 = boto.connect_s3()

bucket = s3.get_bucket('music.tm')


def allowed_file(_filename):
    return '.' in _filename and _filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def upload_track (_params):
    key = bucket.new_key(_params['filename'])

    key.set_contents_from_file(_params['file'], policy='public-read')

