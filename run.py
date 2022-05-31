from app import app
from app.models import db, Character
from app.models import db, User
from app.models import db, Post

@app.shell_context_processor
def shell_context():
    return{'db': db, 'Character': Character, 'User': User, 'Post': Post} 