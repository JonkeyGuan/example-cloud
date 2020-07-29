#!flask/bin/python
# -- coding: utf-8 --

__author__ = 'leo666'

from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return "test public github branch"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
