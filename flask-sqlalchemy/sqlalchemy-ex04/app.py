from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#------------------------------------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
#------------------------------------------
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    tags = db.relationship('Tag', secondary=tags, backref=db.backref('pages', lazy='dynamic'))
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Page %r>' % self.title

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50))
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return '<Tag %r>' % self.label
#------------------------------------------
db.create_all()

tagpython = Tag('python')
tagtuts = Tag('tutorial')
tagjava = Tag('java')
db.session.add(tagpython)
db.session.add(tagjava)
db.session.add(tagtuts)
#db.session.commit()

pagepython1 = Page('pagepython 1')
pagepython2 = Page('pagepython 2')
pagejava = Page('pagejava')
db.session.add(pagepython1)
db.session.add(pagepython2)
db.session.add(pagejava)
#db.session.commit()

pagepython1.tags.append(tagpython)
pagepython1.tags.append(tagtuts)
pagepython2.tags.append(tagpython)
pagejava.tags.append(tagjava)
db.session.commit()

print tagpython.pages.all()
print pagepython1.tags

#print otong.addresses.first()
#print ujang.addresses.all()
#print otongemail1.person

#------------------------------------------
