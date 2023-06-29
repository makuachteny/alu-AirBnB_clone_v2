#!/usr/bin/python3
""" Bash script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Hello HBNB! """
    return "Hello HBNB!"

def hbnb():
    """ HBNB! """
    return "HBNB"

if __name__ == '__main__':
    """ starts the flask app """
    app.run(host='0.0.0.0', port=5000)
