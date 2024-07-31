from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_no = db.Column(db.String(100), nullable=False)
    product_name = db.Column(db.String(200), nullable=False)
    buying_price = db.Column(db.Numeric(10, 2), nullable=False)
    selling_price = db.Column(db.Numeric(10, 2), nullable=False)

    @property
    def profit(self):
        return self.selling_price - self.buying_price
