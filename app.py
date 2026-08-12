from flask import FlaskDoesNotExist, jsonify
from flask import Flask, jsonify

app = Flask(__name__)

# Simulated Naga Supermarket Product Catalog
PRODUCTS = [
    {"id": 1, "name": "Fresh Milk (1L)", "price": 120.00},
    {"id": 2, "name": "Organic Eggs (12pk)", "price": 180.00},
    {"id": 3, "name": "Jasmine Rice (5kg)", "price": 350.00}
]

@app.route('/')
def home():
    return """
    <h1>🛒 Welcome to Naga Supermarket</h1>
    <p>Status: <strong>Online</strong></p>
    <p>Accepted Payments: <strong>GCash, Maya, Card</strong></p>
    <hr>
    <h3>Available Groceries:</h3>
    <ul>
        <li>Fresh Milk (1L) - ₱120.00</li>
        <li>Organic Eggs (12pk) - ₱180.00</li>
        <li>Jasmine Rice (5kg) - ₱350.00</li>
    </ul>
    """

@app.route('/api/products')
def get_products():
    return jsonify({"store": "Naga Supermarket", "products": PRODUCTS})

if __name__ == '__main__':
    # Run server locally on port 5000
    app.run(host='0.0.0.0', port=5000)
