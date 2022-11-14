from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("categories/<int:category_id>",
         views.detail_category, name='category_detail'),
    path('<int:pk>', views.DetailView.as_view(), name='product_detail'),
    path('<int:product_id>/add_stock', views.add_stock, name='add_stock'),
    # path("create", views.IndexView, name='create_product'),
]
