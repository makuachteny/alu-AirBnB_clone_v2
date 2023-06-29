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

@app.route('/number/<n>', strict_slashes=False)
def n_is_number(n):
    """ Displays 'n is a number' only if n is an integer"""
    n = int(n)
    return '{} is a number'.format(n)

@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
        """Displays a HTML page only if n is an integer"""
        n = int(n)
        return render_template('5-number.html', n=n)

if __name__ == '__main__':
    """ starts the flask app """
    app.run(host='0.0.0.0', port=5000)
