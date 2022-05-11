from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String(255))
    passwd = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

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