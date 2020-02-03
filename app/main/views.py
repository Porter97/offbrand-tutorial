from flask import render_template

from . import main


# Index
@main.route('/')
def index():
    return render_template('index.html')
