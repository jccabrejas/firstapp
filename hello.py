# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 14:27:17 2017

@author: Pythonista
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    