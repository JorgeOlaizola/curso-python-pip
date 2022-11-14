import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
from .models import Category, Product

# Create your tests here.

# Models / Vistas


class CategoryModelTests(TestCase):

    def test_was_created_recently_with_future_categories(self):
        """ was_published_recently returns False for categories whose created_at attribute is in the future """
        time = timezone.now() + datetime.timedelta(days=30)
        future_category = Category(
            name="Category", image='image', description='Descriptions test', created_at=time)
        self.assertIs(future_category.was_created_recently(), False)


def create_category(name):
    return Category.objects.create(name=name, description='Description', image='Image', created_at=timezone.now())


def create_product(name, days, id):
    """
    Create a Product with the given "name", and create the given number 
    of days offset to now (negative for products published in the past,
    positive for products that have yet to be created)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Product.objects.create(name=name, created_at=time, description='Description', image='Image', category_id=id)


class ProductIndexViewTests(TestCase):

    def test_no_products(self):
        """If there isnt any product, an appropiate message is displayed"""
        response = self.client.get(reverse("products:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No products are available")
        self.assertQuerysetEqual(response.context["latest_product_list"], [])

    def test_future_products(self):
        """It shouldnt return products that are not created yet"""
        create_category('Technology')
        create_product("Teleporter", days=30, id=1)
        response = self.client.get(reverse("products:index"))
        self.assertContains(response, "No products are available")
        self.assertQuerysetEqual(response.context["latest_product_list"], [])

    def test_past_products(self):
        """Products with a created_at value in the past should be displaye on the index page"""
        create_category('Technology')
        product = create_product(name="Telegram", days=-5, id=1)
        response = self.client.get(reverse("products:index"))
        self.assertQuerysetEqual(
            response.context["latest_product_list"], [product])

    def test_future_products_and_past_products(self):
        """ 
        Even if both past and future products exists,
        only past products are displayed
        """
        create_category('Technology')
        future_product = create_product(name="Teleporter", days=30, id=1)
        past_product = create_product(name="Telegram", days=-5, id=1)
        response = self.client.get(reverse('products:index'))
        self.assertQuerysetEqual(
            response.context["latest_product_list"], [past_product])

    def test_two_past_products(self):
        """The products index page may display multiple products"""
        create_category('Technology')
        past_product = create_product(name="Telegram", days=-30, id=1)
        past_product_2 = create_product(name="Coin", days=-20, id=1)
        response = self.client.get(reverse('products:index'))
        self.assertQuerysetEqual(response.context["latest_product_list"], [
                                 past_product, past_product_2])

    def test_two_future_products(self):
        """The products index page may not display future products"""
        create_category('Technology')
        future_product = create_product(name="Teleporter", days=30, id=1)
        future_product_2 = create_product(name="Time traveler", days=20, id=1)
        response = self.client.get(reverse('products:index'))
        self.assertQuerysetEqual(response.context["latest_product_list"], [])


class ProductDetailViewTests(TestCase):

    def test_future_product(self):
        """ The detail view of a product with a created_at value in the future
        returns a 404 error not found"""
        create_category('Technology')
        future_product = create_product(name="Teleporter", days=30, id=1)
        url = reverse('products:product_detail', args=(future_product.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_product(self):
        """ The detail view of a product with a created_at value in the past
        display the product name """
        create_category('Technology')
        past_product = create_product(name="Teleporter", days=-30, id=1)
        url = reverse('products:product_detail', args=(past_product.id,))
        response = self.client.get(url)
        self.assertContains(response, past_product.name)
