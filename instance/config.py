import os


DEBUG = True

# App directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# App name
APP_NAME = "Music Drop Box"

# Threads per core
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "46100057d51c1023677cce73d3ee652a"

# Secret key for signing cookies
SECRET_KEY = "3c135fcaca9a1f1108132c9453f547cb"

# Freedom Accounts URL
FACCOUNTS_URL = 'http://api.accounts.freedom.tm:80'

# CORS
ALLOWED_HEADERS = ['mida', 'Access-Token', 'nida']
ALLOWED_ORIGINS = '*'
ALLOWED_METHODS = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE']

# Admin Scopes
ADMIN_SCOPES = ['user.info', 'user.delete', 'music.list', 'music.add', 'music.delete', 'music.meta', 'music_provider.add']

# Staff Scopes
STAFF_SCOPES = ['user.info', 'music.list', 'music.add', 'music.meta']

# User
USERS_FIELDS = ['active', 'rank', 'genre', 'mood', 'instrument']

# Music Providers
MUSIC_PROVIDERS_FIELDS = ['name', 'description', 'owner', 'image', 'logo', 'banner', 'website', 'email', 'contact_numbers']

# Tracks
TRACKS_FIELDS = ['title', 'artist', 'album', 'genre', 'mood', 'instrument', 'lyrics', 'country']


print " * Loading config for " + APP_NAME
