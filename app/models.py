from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String(255))
    passwd = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __repr__(self):
        return f'{self.username}'

class WorkTime(db.Model):

    __tablename__ = 'work_time'

    id = db.Column(db.Integer, primary_key = True)
    current_time = db.Column(db.DateTime, default = datetime.now)
    time_chosen = db.Column(db.String(255))

    def __repr__(self):
        return f'{self.current_time}'

class BreakTime(db.Model):

    __tablename__ = 'break_time'

    id = db.Column(db.Integer, primary_key = True)
    current_time = db.Column(db.DateTime, default = datetime.now)
    time_chosen = db.Column(db.String(255))

    def __repr__(self):
        return f'{self.current_time}'