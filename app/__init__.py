from flask import Flask
from config import Config
from .auth.routes import auth
from .models import db, login
from flask_migrate import Migrate
from .api.routes import api
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(Config)
app.config['CORS_HEADERS']='Content-Type'

app.register_blueprint(auth)
app.register_blueprint(api)

#link of communication between app and db
db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'auth.login'
login.login_message = 'Please log in to see this page.'
login.login_message_category = 'danger'


# CORS(app, origins='*')
from . import routes
