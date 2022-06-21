from flask_login import login_required
from app import app
from flask import render_template
from .models import User, Post, db
from flask_cors import CORS, cross_origin

@app.route('/')
@cross_origin()
def home():
    test = 'hello'
    print(test)

    return render_template('index.html', test=test)



@app.route('/about')
@cross_origin()
def about():
    about = 'The story so far...'
    story = 'msms'
    print(about)
    return render_template('about.html', about=about, story=story)

@app.route('/weapons', methods=['GET'])
@cross_origin()
@login_required
def weapons():
    weapons = 'Pulling from database...'
    print(weapons)
    return render_template('weapons.html', weapons=weapons)


@app.route('/blog/<string:username>', methods =['GET'])
@cross_origin()
def userProfile(username):
    user = User.query.filter_by(username=username).first()
    posts = Post.query.filter_by(author=user.id).all()
    for p in posts:
        p.timestamp = str(p.timestamp)[:-7]
    return render_template('profile.html', user=user, posts=posts)


@app.route('/vehicles')
@cross_origin()
def vehicles():
    vehicles = 'The vehicles so far...'
    print(vehicles)
    return render_template('vehicles.html', vehicles=vehicles)

@app.route('/specialitems')
@cross_origin()
def specialitems():
    specialitems = 'The special items so far...'
    print(specialitems)
    return render_template('specialitems.html', specialitems=specialitems)


@app.route('/cart', methods=['GET'])
@cross_origin()
def cart():
    cart = 'The cart items so far...'
    print(cart)
    return render_template('cart.html', cart=cart)