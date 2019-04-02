from django.test import TestCase
from inventory.models import Product
from sales.models import Customer, SoldProduct, SalesOrder, SalesOrderLine


class SalesTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="product 1", quantity=10.00)
        Customer.objects.create(
            name="customer 1", address="test address", postcode="test"
        )
        product = Product.objects.get(name="product 1")
        customer = Customer.objects.get(name="customer 1")
        SoldProduct.objects.create(
            customer=customer, product=product, name="s_product 1", price=0.50
        )
        self.sp = SoldProduct.objects.get(name="s_product 1")
        SalesOrder.objects.create(pk=1, customer=customer)
        so = SalesOrder.objects.get(pk=1)
        SalesOrderLine.objects.create(
            pk=1, sales_order=so, product=self.sp, quantity=10.00, shipped_quantity=0.00
        )
        self.so_line = SalesOrderLine.objects.get(pk=1)

    def test_sold_product_allocated_as_sold(self):
        self.assertEqual(self.sp.sold(), 10.00)

    def test_product_allocated_as_sold(self):
        product = Product.objects.get(name="product 1")
        self.assertEqual(product.sold(), 10.00)

    def test_sale_of_products(self):
        self.assertEqual(self.so_line.complete, False)
        product = Product.objects.get(name="product 1")
        self.assertEqual(product.quantity, 10.00)
        self.so_line.shipped_quantity = 8.00
        self.so_line.complete = True
        self.so_line.save()
        product = Product.objects.get(name="product 1")
        self.assertEqual(product.quantity, 2.00)
