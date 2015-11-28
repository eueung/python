from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#------------------------------------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
#------------------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
#------------------------------------------
db.create_all()

admin = User('admin', 'admin@example.com')
guest = User('guest', 'guest@example.com')
me = User('me', 'me@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.add(me)
db.session.commit()

print me.id #after commit

db.session.delete(me)
db.session.commit()

admin = User.query.filter_by(username='admin').first()
print admin.id
print admin.email

missing = User.query.filter_by(username='missing').first()
print missing is None

print User.query.all()
print User.query.filter(User.email.endswith('@example.com')).all()
print User.query.order_by(User.username).all()
print User.query.limit(1).all() # 1 user
print User.query.get(1) # by primarykey

#------------------------------------------
