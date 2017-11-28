from flask import render_template

from app import app


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/show-template')
def show_template():
    return render_template("template.html")
