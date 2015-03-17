from sqlalchemy import MetaData, Table
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base

from app import app


db = app.db
Base = declarative_base()
metadata = MetaData(bind=app.db.music_db.get_bind())


class BaseModel(Base):
    __table__ = Table('users', metadata, autoload=True)

    def __init__(self, table_name):
        __table__ = Table(table_name, metadata, autoload=True)


    def to_dict(self):
        return { c.name: getattr(self, c.name) for c in self.__table__.columns }


    def select(self, _params={}):
        result = []
        data = db.music_db.query(BaseModel).filter_by(**_params)

        for row in data:
            result.append(row.to_dict())

        return result


    def insert(self, _params):
        db.music_db.execute(self.__table__.insert().values(**_params))
        db.music_db.commit()
        db.music_db.close()


    def update(self, _params):
        db.music_db.execute(self.__table__.update().where(sef.__table__.c))

