#!/usr/bin/python3
""" funtion Starts a Flash Web Application Python is Cool"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ funtion Prints a Message when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """funtion Prints a Message when /hbnb is called """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ funtion Prints a Message when /c is called """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """ funtion Prints a Message when /python is called """
    return "Python " + text.replace('_', ' ')

if __name__ == "__main__":
    """ This Main Function """
    app.run(host='0.0.0.0', port=5000)
