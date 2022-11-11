#!/usr/bin/python3
"""
Script that starts a Flask web application listening on 0.0.0.0:5000
Route / display"Hello HBNB!"
Must use option 'strict_slashes=False'
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """
    Prints Hello HBNB!
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")