from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Estás en la página principal de la aplicación /products/")


def detail_category(request, category_id):
    return HttpResponse(f"Estás viendo la categoría número {category_id}")


def detail_product(request, product_id):
    return HttpResponse(f"Estás viendo el producto número {product_id}")


def add_stock(request, product_id):
    return HttpResponse(f"Estás agregando stock al producto número {product_id}")
