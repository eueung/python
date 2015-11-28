import sqlite3
from flask import Flask, g
#------------------------------------
DATABASE = 'database.db'
app = Flask(__name__)
app.config.from_object(__name__)
#------------------------------------
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
#------------------------------------
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv        
#------------------------------------
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db
#------------------------------------
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
#------------------------------------
#------------------------------------
def seed_db():
    with app.app_context():
        db = get_db()
        seedusers = [('ujang',), ('otong',),]
        db.executemany('INSERT INTO users (username) VALUES (?)', seedusers)
        #db.execute("INSERT INTO users (username) VALUES ('ujang')") 
        #db.execute("INSERT INTO users (username) VALUES ('otong')")
        db.commit()
#------------------------------------
def print_db():
  with app.app_context():
    for user in query_db('select * from users'):
      print user['username'], 'has the id', user['id']
def print_db_one(the_username):
  with app.app_context():
    user = query_db('select * from users where username = ?', [the_username], one=True)
    if user is None:
      print 'No such user'
    else:
      print the_username, 'has the id', user['id']
#------------------------------------
def close_db():
  with app.app_context():
    db = getattr(g, '_database', None)
    if db is not None: db.close()
#------------------------------------
init_db()
seed_db()
print_db()
print_db_one('otong')
close_db()
#---------------------------------------------
