from django.test import TestCase
from purchase.models import Supplier, SupplierContact


class SupplierTestCase(TestCase):
    def setUp(self):
        Supplier.objects.create(
            name="supplier 1", address="test address", postcode="test"
        )
        self.supplier = Supplier.objects.get(name="supplier 1")
        SupplierContact.objects.create(
            supplier=self.supplier, first_name="Hello", last_name="World!"
        )
        self.supplier_contact = SupplierContact.objects.get(supplier=self.supplier)

    def test_supplier(self):
        supplier = Supplier.objects.get(name="supplier 1")
        self.assertEqual(supplier.__str__(), "supplier 1")

    def test_supplier_contact(self):
        self.assertEqual(self.supplier_contact.__str__(), "Hello World!")
