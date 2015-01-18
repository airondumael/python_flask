#put here all module dependedent functions to be called in the main function
from app import app, earnings_db
from lib import database
from lib.error_handler import FailedRequest

config = app.config

def get_access_token (_data):
    
    params = {
        'report_id': 1418022995
    }

    # raise FailedRequest('error', status_code=402)
    # data = earnings_db.execute("select * from report where id = 12345", params)
    # # print data.keys()
    # for row in data:
    #     for col, val in row.items():
    #         print col + ': ' + val

    data = database.query(earnings_db, 'insert into temp values("hahahahaha")', ())
    # data = database.get(earnings_db, 'select * from report', (), False)

    return data


# Accepts {'username': '', 'password': ''} data format
# Returns user_data or error message
def check_login (_data):
    if 'username' in _data and 'password' in _data:
        return True
