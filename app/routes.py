from flask_login import login_required
from app import app
from flask import render_template
from .models import User, Post, db

@app.route('/')
def home():
    test = 'hello'
    print(test)

    return render_template('index.html', test=test)

@app.route('/about')
def about():
    about = 'The story so far...'
    story = 'msms'
    print(about)
    return render_template('about.html', about=about, story=story)

@app.route('/characters', methods=['GET'])
@login_required
def characters():
    characters = 'we r going ot havr to oull from the db for this one'
    print(characters)
    return render_template('characters.html', characters=characters)


@app.route('/blog/<string:username>', methods =['GET'])
def userProfile(username):
    user = User.query.filter_by(username=username).first()
    posts = Post.query.filter_by(author=user.id).all()
    for p in posts:
        p.timestamp = str(p.timestamp)[:-7]
    return render_template('profile.html', user=user, posts=posts)