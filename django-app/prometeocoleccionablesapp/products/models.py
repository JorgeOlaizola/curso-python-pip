from django.db import models
from django.utils import timezone
import datetime


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510)
    image = models.CharField(max_length=1000)
    created_at = models.DateTimeField("Created at")

    def __str__(self):
        return self.name

    def was_created_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510)
    image = models.CharField(max_length=1000)
    created_at = models.DateTimeField("Created at")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Borra todos los products cuando se borra una categoría
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
