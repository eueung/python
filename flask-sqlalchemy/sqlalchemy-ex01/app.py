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

db.session.add(admin)
db.session.add(guest)
db.session.commit()

users = User.query.all()
print users

admin = User.query.filter_by(username='admin').first()
print admin
#------------------------------------------
#if __name__ == '__main__':
#    app.run(debug=True)