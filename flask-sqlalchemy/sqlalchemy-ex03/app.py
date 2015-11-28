from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#------------------------------------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
#------------------------------------------
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    addresses = db.relationship('Address', backref='person', lazy='dynamic')
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Person %r>' % self.name

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    #person = db.relationship('Person', backref=db.backref('addresses', lazy='dynamic'))
    def __init__(self, email,pers):
        self.email = email
        self.person_id = pers.id

    def __repr__(self):
        return '<Address %r>' % self.email
#------------------------------------------
db.create_all()

otong = Person('otong')
ujang = Person('ujang')
db.session.add(otong)
db.session.add(ujang)
db.session.commit()

otongemail1 = Address('otong@example.com',otong)
otongemail2 = Address('otong@nasa.com',otong)
ujangemail = Address('ujang@example.com',ujang)
db.session.add(otongemail1)
db.session.add(otongemail2)
db.session.add(ujangemail)
db.session.commit()

print otong.addresses.all()
print otong.addresses.first()
print ujang.addresses.all()
print otongemail1.person

#------------------------------------------
