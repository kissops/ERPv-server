from decimal import Decimal
from django.test import TestCase
from inventory.models import Product, Location, LocationQuantity, Warehouse


class LocationTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="product 1", quantity=0.00)
        self.product = Product.objects.get(name="product 1")
        Warehouse.objects.create(name="warehouse 1")
        self.warehouse = Warehouse.objects.get(name="warehouse 1")
        Location.objects.create(warehouse=self.warehouse, name="location 1")
        self.location = Location.objects.get(name="location 1")
        LocationQuantity.objects.create(
            product=self.product, location=self.location, quantity=Decimal(0.00)
        )

    def test_inventory_location(self):
        self.assertEqual(self.location.name, "location 1")
        self.assertEqual(self.location.__str__(), "location 1")
        self.assertEqual(self.location.location_warehouse(), "warehouse 1")

    def test_inventory_location_quantity(self):
        locationquantity = LocationQuantity.objects.get(location=self.location)
        self.assertEqual(locationquantity.quantity, Decimal(0.00))
        self.assertEqual(locationquantity.product_name(), "product 1")
        self.assertEqual(
            locationquantity.__str__(),
            f"{self.product} {self.location} {locationquantity.quantity}",
        )
        self.assertEqual(locationquantity.location_name(), "location 1")
        self.assertEqual(locationquantity.location_warehouse(), "warehouse 1")
