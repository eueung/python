from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String

engine = create_engine('sqlite:///test.db', convert_unicode=True)
metadata = MetaData(bind=engine)

users = Table('users', metadata,  
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('email', String(120), unique=True)
)
metadata.create_all(bind=engine)
#users = Table('users', metadata, autoload=True)
#if previously exists

con = engine.connect()
con.execute(users.insert(), name='admin', email='admin@localhost')
# SQLAlchemy will automatically commit for us.

print users.select(users.c.id == 1).execute().first()
r = users.select(users.c.id == 1).execute().first()
print  r['name']
print engine.execute('select * from users where id = :1', [1]).first()
#------------------------------------------