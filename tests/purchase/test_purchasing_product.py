from django.test import TestCase
from inventory.models import Product
from purchase.models import Supplier, PurchasedProduct, PurchaseOrder, PurchaseOrderLine


class PurchaseTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="product 1", quantity=0.00)
        Supplier.objects.create(
            name="supplier 1", address="test address", postcode="test"
        )
        product = Product.objects.get(name="product 1")
        supplier = Supplier.objects.get(name="supplier 1")
        PurchasedProduct.objects.create(
            supplier=supplier, product=product, name="s_product 1", cost=0.50
        )
        self.pp = PurchasedProduct.objects.get(name="s_product 1")
        PurchaseOrder.objects.create(pk=1, supplier=supplier)
        po = PurchaseOrder.objects.get(pk=1)
        PurchaseOrderLine.objects.create(
            pk=1,
            purchase_order=po,
            product=self.pp,
            quantity=10.00,
            received_quantity=0.00,
        )
        self.po_line = PurchaseOrderLine.objects.get(pk=1)

    def test_purchased_product_allocated_as_purchased(self):
        self.assertEqual(self.pp.on_order(), 10.00)

    def test_product_allocated_as_purchased(self):
        product = Product.objects.get(name="product 1")
        self.assertEqual(product.purchased(), 10.00)

    def test_receipt_of_products(self):
        self.assertEqual(self.po_line.complete, False)
        product = Product.objects.get(name="product 1")
        self.assertEqual(product.quantity, 0.00)
        self.po_line.received_quantity = 15.00
        self.po_line.complete = True
        self.po_line.save()
        product = Product.objects.get(name="product 1")
        self.assertEqual(product.quantity, 15.00)
