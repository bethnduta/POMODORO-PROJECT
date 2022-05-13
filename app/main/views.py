from crypt import methods
from . import main
from flask import render_template, url_for, redirect, request, session
from app import db
from ..models import User
from config import Config
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash

main.secret_key = Config.SECRET_KEY
main.permanent_session_lifetime = timedelta(weeks=1)


@main.route('/')
def home():
    return render_template('home.html')
     
@main.route('/work')
def work(): 
    return render_template('work.html') 

@main.route('/user-login')
def templogin(): 
    return render_template('login.html') 

@main.route('/user-signup')
def tempsignup(): 
    return render_template('signup.html') 




@main.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        present_user = User.query.filter_by(username=request.form['username']).first()
        if present_user:
            print("user exists")
            # add a flash message that a user exists
            return redirect(url_for('main.home'))
        else:
            user = User(username=request.form["username"], passwd=generate_password_hash(request.form["s-password"]))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.work'))
    else:
        return redirect(url_for('main.home'))



@main.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['l-email']).first()
        if user:
            if check_password_hash(user.password, request.form['l-password']) == True:
                session["user"] = user.name
                return redirect(url_for('user', username = user.name), code=307)
            else:
                # add password or username wrong flash message
                return redirect(url_for('main.home'))
        else:
             # add signup flashmessage
            return redirect(url_for('main.home'))
    else:
        return redirect(url_for('main.home'))


@main.route('/logout')
def sign_out():
    session.clear()
    return redirect(url_for('main.home'))