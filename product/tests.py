from django.test import TestCase
from slugify import slugify

from product.repository import ProductRepository

repo = ProductRepository()

class APIProductTestCase(TestCase):
    def setUp(self):
        laptop = repo.create_product({
            "name": "Laptop HP",
            "slug": slugify("Laptop HP"),
            "price": 2500000
        })

    def test_product_created_properly(self):
        laptop = repo.get_product_by_slug("laptop-hp")

        self.assertEqual(laptop is not None, True)
        self.assertEqual(laptop.id, 1)
        self.assertEqual(laptop.name, "Laptop HP")
        self.assertEqual(laptop.price, 2500000)

    def test_product_not_found(self):
        laptop = repo.get_product_by_slug("laptop-hp-random")

        self.assertEqual(laptop is None, True)
