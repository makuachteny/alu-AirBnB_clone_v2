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

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Displays 'C' followed by the values
    replacing underscores with spaces """
    text = text.replace("_", " ")
    return 'C{}'.format(text.replace('_', ' '))

@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """ Displays 'Python' followed by the values
    replacing underscores with spaces """
    text = text.replace("_", " ")
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    """ starts the flask app """
    app.run(host='0.0.0.0', port=5000)
