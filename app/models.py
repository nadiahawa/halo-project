from flask_sqlalchemy import SQLAlchemy
from psycopg2 import Timestamp
from sqlalchemy import LABEL_STYLE_TABLENAME_PLUS_COL, PrimaryKeyConstraint

db = SQLAlchemy()

from flask_login import LoginManager, UserMixin
from datetime import datetime
from uuid import uuid4
from werkzeug.security import generate_password_hash

login = LoginManager()

@login.user_loader
def load_user(userid):
    return User.query.get(userid)


class Weapons(db.Model):
    id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    species = db.Column(db.String(100), nullable = False)
    affiliation = db.Column(db.String(100), default=None)
    image = db.Column(db.String(255), default=None)
    creator = db.Column(db.String(255), db.ForeignKey('user.id'))
    price = db.Column(db.Float(50), default=None)
    quantity = db.Column(db.Float(50), default=None)

    def __init__(self, dict):
        self.id = str(uuid4())
        self.name = dict['name'].title()
        self.species = dict['species'].title()
        self.affiliation = dict.get('affiliation')
        self.image = dict.get('image')
        self.creator = dict.get('creator')
        self.price = dict.get('price')
        self.quantity = dict.get('quantity')
        

    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'species' : self.species,
            'affiliation' : self.affiliation,
            'image' : self.image,
            'creator': self.creator,
            'price': self.price,
            'quantity' : self.quantity
        }

    def from_dict(self, dict):
        for key in dict:
            setattr(self, key, dict[key])
            # self.id = dict.get('id')
            # self.name = dict.get('name')
            # self.species = dict.get('species')
            # self.affiliation = dict.get('affiliation')
            # self.image = dict.get('image')



class User(db.Model, UserMixin):
    id = db.Column(db.String(40), primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(255), default='No bio.')
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    created = db.Column(db.DateTime, default=datetime.utcnow())
    api_token = db.Column(db.String(100))
    posts = db.relationship('Post', backref ='post_author')
    carts = db.Column(db.Integer, db.ForeignKey('cart.id'))
    # new_user = User(username=user_data['username'])

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password)
        self.carts = dict.get('carts')

    def to_dict(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'carts' : self.carts,

        }
        

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(255), nullable = False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
    author = db.Column(db.String, db.ForeignKey('user.id'))


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    def __init__(self):
        self.id = str(uuid4())
        

class Cartitems(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    item = db.Column(db.String(255))
    cart = db.Column(db.Integer, db.ForeignKey('cart.id'))
    item_type = db.Column(db.String(255))

    def __init__(self, dict):
        self.item = dict.get('item')
        self.cart = dict.get('cart')
        self.item_type = dict.get('item_type')
        
        

    def to_dict(self):
        return {
            'id' : self.id,
            'item' : self.item,
            'cart' : self.cart,
            'item_type' : self.item_type,

        }



class Vehicles(db.Model):
    id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    affiliation = db.Column(db.String(100), default=None)
    image = db.Column(db.String(255), default=None)
    price = db.Column(db.Float(50), default=None)
    quantity = db.Column(db.Float(50), default=None)

    def __init__(self, dict):
        self.id = str(uuid4())
        self.name = dict['name'].title()
        self.affiliation = dict.get('affiliation')
        self.image = dict.get('image')
        self.price = dict.get('price')
        self.quantity = dict.get('quantity')
        

    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'affiliation' : self.affiliation,
            'image' : self.image,
            'price': self.price,
            'quantity' : self.quantity
        }

    def from_dict(self, dict):
        for key in dict:
            setattr(self, key, dict[key])


class Special(db.Model):
    id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    affiliation = db.Column(db.String(100), default=None)
    image = db.Column(db.String(255), default=None)
    price = db.Column(db.Float(50), default=None)
    quantity = db.Column(db.Float(50), default=None)

    def __init__(self, dict):
        self.id = str(uuid4())
        self.name = dict['name'].title()
        self.affiliation = dict.get('affiliation')
        self.image = dict.get('image')
        self.price = dict.get('price')
        self.quantity = dict.get('quantity')
        

    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'affiliation' : self.affiliation,
            'image' : self.image,
            'price': self.price,
            'quantity' : self.quantity
        }

    def from_dict(self, dict):
        for key in dict:
            setattr(self, key, dict[key])
