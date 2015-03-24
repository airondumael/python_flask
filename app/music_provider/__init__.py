# Import app-based dependencies
from app import app

# Import core libraries
from lib import database


db = app.db


def add_music_provider(_params):
    data = database.query(db.music_db, 'INSERT INTO music_providers VALUES(:id, :name, :description, \
        :owner, :image, :logo, :banner, :website, :email, :contact_numbers, :date_created, NULL)', _params)

    return data

