from app import app
from app.models import Cartitems, Vehicles, db, Character, Special
from app.models import db, User
from app.models import db, Cart
from app.models import db, Post
from app.models import db, Cartitems

@app.shell_context_processor
def shell_context():
    return{'db': db, 'Character': Character, 'User': User, 'Post': Post, 'Cart': Cart, 'Cartitems': Cartitems, 'Vehicles': Vehicles, 'Special': Special} 