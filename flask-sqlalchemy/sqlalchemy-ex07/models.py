from sqlalchemy import Column, Integer, String
#from database import Base
from sqlalchemy import Table
from sqlalchemy.orm import mapper
from database import metadata, db_session
#------------------------------------------
#class User(Base):
class User(object):
    #__tablename__ = 'users'
    #id = Column(Integer, primary_key=True)
    #name = Column(String(50), unique=True)
    #email = Column(String(120), unique=True)
    query = db_session.query_property()

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)
#------------------------------------------
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('email', String(120), unique=True)
)
mapper(User, users)
#------------------------------------------