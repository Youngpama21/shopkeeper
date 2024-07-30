from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    total_profit = sum(product.profit for product in products)
    return render(request, 'shop/templates/shop/product_list.html', {'products': products, 'total_profit': total_profit})
