#!/usr/bin/python3
"""Flask web application."""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """Display C then text."""
    return f"C {escape(text).replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Display python then text."""
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
