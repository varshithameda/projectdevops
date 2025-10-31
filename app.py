from flask import Flask, render_template

app = Flask(__name__)

# Sample products
products = [
    {"id": 1, "name": "Smartphone", "price": 699, "desc": "Latest 5G smartphone"},
    {"id": 2, "name": "Laptop", "price": 999, "desc": "Lightweight and powerful"},
    {"id": 3, "name": "Headphones", "price": 199, "desc": "Noise-cancelling headset"},
]

@app.route('/')
def home():
    return render_template("index.html", products=products)

@app.route('/product/<int:pid>')
def product_page(pid):
    product = next((p for p in products if p["id"] == pid), None)
    if not product:
        return "Product not found", 404
    return render_template("product.html", product=product)

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
