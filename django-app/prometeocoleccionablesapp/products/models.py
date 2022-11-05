from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510)
    image = models.CharField(max_length=1000)
    created_at = models.DateTimeField("Created at")


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510)
    image = models.CharField(max_length=1000)
    created_at = models.DateTimeField("Created at")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Borra todos los products cuando se borra una categoría
    stock = models.IntegerField(default=0)
