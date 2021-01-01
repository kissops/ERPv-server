from django.test import TestCase
from inventory.models import Product
from manufacturing.models import Job


class JobTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="product 1", quantity=0.00)
        self.product = Product.objects.get(name="product 1")
        Job.objects.create(pk=1, product=self.product, quantity=10.00, priority=1)
        self.job = Job.objects.get(pk=1)

    def test_job(self):
        self.assertEqual(self.job.__str__(), self.product.name)

    def test_product_allocated_as_planned(self):
        self.assertEqual(self.product.planned(), 10.00)

    def test_production_of_products(self):
        self.assertEqual(self.job.complete, False)
        self.assertEqual(self.product.quantity, 0.00)
        self.job.bom_allocated = True
        self.job.complete = True
        self.job.save()
        product = Product.objects.get(name="product 1")
        self.assertEqual(product.quantity, 10.00)
