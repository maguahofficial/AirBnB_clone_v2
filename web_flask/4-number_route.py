#!/usr/bin/python3
""" Function Starts a Flash Web Application Python is Cool"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function Prints a Message when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function Prints a Message when /hbnb is called """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Function Prints a Message when /c is called """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """ Function Prints a Message when /python is called """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_n_number(n):
    """ Function Prints a Message when /number is called only if n is an int"""
    return "{:d} is a number".format(n)

if __name__ == "__main__":
    """The Main Function """
    app.run(host='0.0.0.0', port=5000)
