from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.


def index(request):
    latest_product_list = Product.objects.all()
    return render(request, "products/index.html", {"latest_product_list": latest_product_list})


def detail_category(request, category_id):
    return HttpResponse(f"Estás viendo la categoría número {category_id}")


def detail_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/detail.html", {"product": product})


def add_stock(request, product_id):
    return HttpResponse(f"Estás agregando stock al producto número {product_id}")
