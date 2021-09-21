from django.test import TestCase
from .models import Product, Customer
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class ProductModelTest(TestCase):

    def setUp(self):
        product = Product()
        product.product_name = 'Hp Laptop'
        product.product_unit = 2
        product.save()

        Product.objects.create(product_name='Dell Laptop', product_unit=1)

    def test_product_label(self):
        product = Product.objects.get(product_unit=2)
        print("Printing the product name here----------->", product)
        self.assertEqual(product.product_name.lower(), "Hp Laptop".lower())

    def product_exists(self):
        count = Product.objects.all().count()
        self.assertEqual(count, 2)

    def test_products_with_equal_unit(self):
        count = Product.objects.filter(product_unit=2).count()
        self.assertEqual(count, 2)

class TestCustomerProfile(TestCase):
    def setUp(self):
        user = User()
        user.username = "admin"
        user.email = "mdiftea@gmail.com"
        user.is_member = True
        user.is_superuser = True
        user.set_password("ifty @@@")
        user.save()

        product = Product()
        product.product_name = 'Hp Laptop'
        product.product_unit = 2
        product.save()

        customer = Customer()
        customer.customer_name = "Ifty"
        customer.user = user
        customer.product = product
        customer.save()

    def test_customer_exist(self):
        count_customers = Customer.objects.all().count()
        self.assertEqual(count_customers, 1)




