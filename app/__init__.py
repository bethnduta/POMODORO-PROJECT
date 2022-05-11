from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options

db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)

    #initialize app extensions
    db.init_app(app)

    # Creating the app configurations

    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    return app
