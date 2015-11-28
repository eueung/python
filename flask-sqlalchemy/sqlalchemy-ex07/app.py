from database import db_session, init_db
from models import User
from flask import Flask
#------------------------------------------
app = Flask(__name__)
#------------------------------------------
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
#------------------------------------------

init_db()

u = User('admin', 'admin@localhost')
db_session.add(u)
db_session.commit()

print User.query.all()
print User.query.filter(User.name == 'admin').first()
#------------------------------------------
