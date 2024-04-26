"""
This module defines a simple containerized Flask application.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """
    This function handles requests to the home page.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"Hi there, Welcome": "Website is under construction"}


if __name__ == "__main__":
    app.run()
