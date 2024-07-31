from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Product
from forms import ProductForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            product_no=form.product_no.data,
            product_name=form.product_name.data,
            buying_price=form.buying_price.data,
            selling_price=form.selling_price.data
        )
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!')
        return redirect(url_for('product_list'))
    return render_template('add_product.html', form=form)

@app.route('/')
def product_list():
    products = Product.query.all()
    total_profit = sum(product.profit for product in products)
    return render_template('product_list.html', products=products, total_profit=total_profit)

if __name__ == '__main__':
    app.run(debug=True)
