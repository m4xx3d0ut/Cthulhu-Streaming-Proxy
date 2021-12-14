import redis
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session.__init__ import Session


db = SQLAlchemy()
sess = Session()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Flask session
app.config['SESSION_COOKIE_NAME'] = 'session_cookie'
app.config['SESSION_TYPE'] = os.environ.get('SESSION_TYPE')
app.config['SESSION_REDIS'] = redis.from_url(os.environ.get('SESSION_REDIS'))

db.init_app(app)
sess.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# # blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)