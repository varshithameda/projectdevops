from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "mysecretkey"  # Needed for session management

# Dummy products
products = [
    {"id": 1, "name": "Smartphone", "price": 699, "desc": "Latest 5G smartphone"},
    {"id": 2, "name": "Laptop", "price": 999, "desc": "Lightweight and powerful"},
    {"id": 3, "name": "Headphones", "price": 199, "desc": "Noise-cancelling headset"},
]

@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("index.html", products=products, username=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            session['username'] = username
            session['cart'] = []
            return redirect(url_for('home'))
        else:
            flash("Please enter a valid username.")
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/product/<int:pid>')
def product_page(pid):
    if 'username' not in session:
        return redirect(url_for('login'))
    product = next((p for p in products if p["id"] == pid), None)
    if not product:
        return "Product not found", 404
    return render_template("product.html", product=product)

@app.route('/add_to_cart/<int:pid>')
def add_to_cart(pid):
    if 'username' not in session:
        return redirect(url_for('login'))
    product = next((p for p in products if p["id"] == pid), None)
    if product:
        session['cart'].append(product)
        flash(f"{product['name']} added to cart!")
    return redirect(url_for('home'))

@app.route('/cart')
def view_cart():
    if 'username' not in session:
        return redirect(url_for('login'))
    cart = session.get('cart', [])
    return render_template("cart.html", cart=cart)

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
