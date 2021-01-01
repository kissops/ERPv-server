from django.test import TestCase
from inventory.models import Warehouse


class WarehouseTestCase(TestCase):
    def setUp(self):
        Warehouse.objects.create(name="warehouse 1")
        self.warehouse = Warehouse.objects.get(name="warehouse 1")

    def test_inventory_location_quantity(self):
        self.assertEqual(self.warehouse.name, "warehouse 1")
        self.assertEqual(self.warehouse.__str__(), "warehouse 1")
        self.assertEqual(self.warehouse.location_count(), 0)
