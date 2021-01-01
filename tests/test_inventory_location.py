from decimal import Decimal
from django.test import TestCase
from inventory.models import Product, Location, LocationQuantity, Warehouse


class InventoryTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="product 1", quantity=0.00)
        product1 = Product.objects.get(name="product 1")
        Warehouse.objects.create(name="warehouse 1")
        warehouse1 = Warehouse.objects.get(name="warehouse 1")
        Location.objects.create(warehouse=warehouse1, name="location 1")
        location1 = Location.objects.get(name="location 1")
        LocationQuantity.objects.create(
            product=product1, location=location1, quantity=Decimal(0.00)
        )

    def test_inventory_location_quantity(self):
        location1 = Location.objects.get(name="location 1")
        locationquantity = LocationQuantity.objects.get(location=location1)
        self.assertEqual(locationquantity.quantity, Decimal(0.00))
