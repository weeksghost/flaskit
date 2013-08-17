from flask import render_template, flash, redirect
from app import app


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index')
def index():
    return render_template("index.html",
        title = 'Ajax Form')

