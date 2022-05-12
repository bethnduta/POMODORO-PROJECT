from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'POMODORO'
    
    #main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    #initialize app extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Creating the app configurations

    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    
    

    return app
