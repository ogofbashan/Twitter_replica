from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config.from_object(Config)

#setup db variables

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
