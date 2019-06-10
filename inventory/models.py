from decimal import Decimal
from django.db import models
from django.urls import reverse
from ledger.models import InventoryLedger


class Warehouse(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def locations(self):
        return self.warehouse_locations.count()

    def get_absolute_url(self):  # new
        return reverse("warehouse_detail", args=[str(self.id)])


class Product(models.Model):
    """
    Product model: 
    """

    name = models.CharField(max_length=128, unique=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    allocated_for_jobs = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    desired_stock_level = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def ledger(self):
        return InventoryLedger.objects.filter(name=self.name)

    def planned(self):
        try:
            jobs = sum(
                [job.quantity for job in self.product_jobs.filter(complete=False)]
            )
            return jobs
        except:
            pass

    def purchased(self):
        try:
            orders = sum(
                [
                    purchased_product.on_order()
                    for purchased_product in self.product_purchased_product.all()
                ]
            )
            return orders
        except:
            pass

    def sold(self):
        try:
            orders = sum(
                [
                    sold_product.sold()
                    for sold_product in self.product_sold_product.all()
                ]
            )
            return orders
        except:
            pass

    def required(self):
        allocated_stock = (
            self.sold() + self.allocated_for_jobs + self.desired_stock_level
        )
        stock_with_orders = (
            self.quantity + Decimal(self.planned()) + Decimal(self.purchased())
        )
        required = stock_with_orders - allocated_stock
        try:
            if required < 0.00:
                return abs(required)
            else:
                return 0
        except:
            return 0

    def get_absolute_url(self):  # new
        return reverse("product_detail", args=[str(self.id)])


class Location(models.Model):
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, related_name="warehouse_locations"
    )
    product = models.ManyToManyField(Product, related_name="product_locations")
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ["name"]
        unique_together = ("warehouse", "name")

    def __str__(self):
        return self.name
