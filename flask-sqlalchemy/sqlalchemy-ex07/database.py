from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
#------------------------------------------
engine = create_engine('sqlite:///test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
metadata = MetaData()
#Base = declarative_base()
#Base.query = db_session.query_property()
#------------------------------------------
def init_db():
    #import models
    #Base.metadata.create_all(bind=engine)
    metadata.create_all(bind=engine)
#------------------------------------------
#------------------------------------------