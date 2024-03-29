from django.shortcuts import render
from .models import Product

def products_by_category(request, category_id):
    category_products = Product.objects.filter(category=category_id)
    return render(request, 'products_by_category.html', {'category_products': category_products})
