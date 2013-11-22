# -*- coding: utf-8 -*-

from oozi import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World"
