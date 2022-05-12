from . import main
from flask import render_template


@main.route('/')
def home():
    return render_template('home.html')
     
     
@main.route('/work')
def work(): 
    return render_template('work.html') 
