from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_no', 'product_name', 'buying_price', 'selling_price']
