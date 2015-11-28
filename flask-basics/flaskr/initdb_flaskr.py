import sqlite3
from flask import Flask
from contextlib import closing
#---------------------------------------------
# configuration
DATABASE = 'flaskr.db'
#DEBUG = True
#SECRET_KEY = 'development key'
#USERNAME = 'admin'
#PASSWORD = 'default'
#---------------------------------------------
app = Flask(__name__)
app.config.from_object(__name__)
#---------------------------------------------
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
#---------------------------------------------
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()    
#---------------------------------------------
init_db()
#---------------------------------------------
#if __name__ == '__main__':
#    app.run()
#---------------------------------------------