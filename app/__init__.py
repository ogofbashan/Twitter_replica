from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config.from_object(Config)

#setup db variables

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# app variable for handling login functionality
login = LoginManager(app)

# when a page requires someone to be logged in, specify the route they should be sent to when accessing that page anonymously

login.login_view = 'login'

from app import routes
