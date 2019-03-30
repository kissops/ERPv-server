from django.test import TestCase
from inventory.models import Product
from manufacturing.models import Job


class ManufacturingTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="product 1", quantity=0.00)
        product = Product.objects.get(name="product 1")
        Job.objects.create(pk=1, product=product, quantity=10.00, priority=1)
        self.job = Job.objects.get(pk=1)

    def test_product_allocated_as_planned(self):
        product = Product.objects.get(name="product 1")
        self.assertEqual(product.planned(), 10.00)

    def test_production_of_products(self):
        self.assertEqual(self.job.complete, False)
        product = Product.objects.get(name="product 1")
        self.assertEqual(product.quantity, 0.00)
        self.job.complete = True
        self.job.save()
        product = Product.objects.get(name="product 1")
        self.assertEqual(product.quantity, 10.00)
