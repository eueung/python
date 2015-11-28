import sqlite3
from flask import Flask, g, jsonify
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
def make_dicts(cur, row):
    return dict((cur.description[idx][0], value)
                for idx, value in enumerate(row))
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    #rv.row_factory = sqlite3.Row
    rv.row_factory = make_dicts
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
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
#------------------------------------
#------------------------------------
@app.route('/')
def index():
    res = query_db('select * from users')
    print res
    return jsonify(results = res)
#------------------------------------    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
#------------------------------------    


#------------------------------------    
#from flask import Response
#import json
    #return Response(json.dumps(res),  mimetype='application/json')
#------------------------------------    
# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d
# jsonify(name=student['name'], age=student['age'])
