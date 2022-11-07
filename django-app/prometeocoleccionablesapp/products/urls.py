from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/<int:category_id>",
         views.detail_category, name='category_detail'),
    path('<int:product_id>', views.detail_product, name='product_detail'),
    path('<int:product_id>/add_stock', views.add_stock, name='add_stock')
]
