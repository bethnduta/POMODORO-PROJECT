from flask import render_template
from flask import render_template
from .import auth

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "logout"

@auth.route('/sign-up')
def sign_up():
    return render_template("signup.html")