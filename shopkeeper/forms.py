from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    product_no = StringField('Product No.', validators=[DataRequired()])
    product_name = StringField('Product Name', validators=[DataRequired()])
    buying_price = DecimalField('Buying Price', validators=[DataRequired()])
    selling_price = DecimalField('Selling Price', validators=[DataRequired()])
    submit = SubmitField('Add Product')
