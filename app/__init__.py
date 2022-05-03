from flask import Flask
from config import config_options
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db=SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing the database
    db.init_app(app)

    # Initializing Flask Extensions
    bootstrap.init_app(app)

     # Registering the blueprint from main.__init__.py
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app