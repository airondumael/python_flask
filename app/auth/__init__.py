#put here all module dependedent functions to be called in the main function
from app import app, earnings_db
from lib import database

config = app.config

def get_access_token (_data):
    
    params = {
        'id' : _data,
        'test': "tessst333"
    }

    # data = earnings_db.execute("select * from report where id = 12345", params)
    # # print data.keys()
    # for row in data:
    #     for col, val in row.items():
    #         print col + ': ' + val

    data = database.query(earnings_db, 'insert into temp values(:id, :test)', params)
    # data = database.get(earnings_db, 'select * from report', (), False)

    return data


# Accepts {'username': '', 'password': ''} data format
# Returns user_data or error message
def check_login (_data):
    if 'username' in _data and 'password' in _data:
        return True
