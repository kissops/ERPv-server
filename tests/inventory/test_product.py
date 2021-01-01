from django.test import TestCase
from inventory.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="product 1", quantity=0.00)
        self.product = Product.objects.get(name="product 1")

    def test_product(self):
        self.assertEqual(self.product.name, "product 1")
        self.assertEqual(self.product.__str__(), "product 1")
        self.assertQuerysetEqual(self.product.ledger(), [])
