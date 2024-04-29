"""
This module defines a simple containerized Flask application.
"""

from flask import Flask, jsonify

app = Flask(__name__)

# Improved database structure with a dictionary for easier access by ID
demo_lib_db = {
    25: {
        "name": "Ashok Madhav",
        "items": {"book_name": "Harry Potter", "Lease period in days": 20},
    },
    20: {
        "name": "Joe John",
        "items": {"book_name": "Python 3.11", "Lease period in days": 15},
    },
    5: {
        "name": "Bijo Joseph",
        "items": {"book_name": "Physics & AI ", "Lease period in days": 45},
    },
}


@app.route("/", methods=["GET"])
def home():
    """
    Handle requests to the home page.

    Returns:
        Response object: JSON response with a welcome message.
    """
    return jsonify(message="Welcome! The website is under construction."), 200


@app.route("/customers", methods=["GET"])
def customer_base():
    """
    Handle requests to the /customers page.

    Returns:
        Response object: JSON response with all customer details.
    """

    # Using dictionary comprehension for a cleaner approach
    customer_list = {cust_id: name["name"] for cust_id, name in demo_lib_db.items()}
    return jsonify(customers=customer_list), 200


if __name__ == "__main__":
    app.run(debug=True)  # Added debug mode for development
