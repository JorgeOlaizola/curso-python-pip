import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Category

# Create your tests here.

# Models / Vistas


class CategoryModelTests(TestCase):

    def test_was_created_recently_with_future_categories(self):
        """ was_published_recently returns False for categories whose created_at attribute is in the future """
        time = timezone.now() + datetime.timedelta(days=30)
        future_category = Category(
            name="Category", image='image', description='Descriptions test', created_at=time)
        self.assertIs(future_category.was_created_recently(), False)
