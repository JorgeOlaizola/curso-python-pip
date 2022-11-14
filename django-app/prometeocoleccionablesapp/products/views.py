from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Product, Category

# Create your views here.


class IndexView(generic.ListView):
    template_name = "products/index.html"
    context_object_name = "latest_product_list"

    def get_queryset(self):
        """Return all created products"""
        return Product.objects.all()


class DetailView(generic.DetailView):
    model = Product
    template_name = "products/detail.html"

# def index(request):
#     latest_product_list = Product.objects.all()
#     return render(request, "products/index.html", {"latest_product_list": latest_product_list})


def detail_category(request, category_id):
    return HttpResponse(f"Estás viendo la categoría número {category_id}")


# def detail_product(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     return render(request, "products/detail.html", {"product": product})


def add_stock(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    option = request.POST["stock"]
    try:
        if option == 'add':
            product.stock = product.stock + 1
        else:
            product.stock = product.stock - 1
    except:
        return render(request, "products/detail.html", {
            "product": product,
            "error_message": 'Hubo un error al actualizar el producto'
        })
    else:
        product.save()
        print(product.id)
        return HttpResponseRedirect(reverse(f"products:product_detail", args=[product.id]))
