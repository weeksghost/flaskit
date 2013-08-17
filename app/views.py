from flask import render_template, redirect
from app import app


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index')
def index():
    return render_template("index.html",
        title = 'Ajax',
        header = 'jQuery Test',
        message = 'Success!')
