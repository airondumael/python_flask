
# Mongo db config
MONGO_URI       = '127.0.0.1'
MONGO_HOST      = 'localhost'
MONGO_PORT      = '27017'
MONGO_CONNECT_TIMEOUT_MS    = 10000



# MySQL Config
# For multiple mysql connections, use object for each config,
# the db driver will read and parse it as needed

MYSQL_EARNINGS = {
    'host'        : 'localhost',
    'db'          : 'earnings_report',
    'user'        : 'root',
    'password'    : '',
    'port'        : 3306
}



MYSQL_MUSIC = {
    'host'      : 'localhost',
    'db'        : 'music_tm',
    'user'      : 'root',
    'password'  : '',
    'port'      : 3306
}



# Freedom Accounts Config
FACCOUNTS_PARAMS = {
    'service'       : 'music_dashboard',
    'redirect_uri'  : 'http://dev.music.tm:3000/auth/callback',
    'response_type' : 'code',
    'roles'         : 'profile,email,partner'
}
