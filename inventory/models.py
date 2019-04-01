from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Warehouse(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    def locations(self):
        return self.warehouse_locations.count()


class Product(models.Model):
    """
    Product model: 
    """

    name = models.CharField(max_length=128, unique=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    allocated = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

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
        try:
            if self.quantity - self.sold() + self.planned() + self.purchased() <= 0.00:
                return (
                    self.sold()
                    - self.planned()
                    - self.purchased()
                    - self.quantity
                    + self.allocated
                )
            else:
                return 0
        except:
            return 0


class BillOfMaterials(models.Model):
    """
    This is the products Bill of Materials.
    ie: an intermediate object to the list of BOMitems that make up the product.
    """

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ["product"]
        verbose_name_plural = "Bill of Materials"

    def __str__(self):
        return self.product.name


class BOMItem(models.Model):
    """
    This model contains the Bill of Material Items.
    ie: the Product and Quantity that go into making a Bill of Materials for a product.
    """

    bom = models.ForeignKey(
        BillOfMaterials, on_delete=models.CASCADE, related_name="bom_items"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_bom_items"
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def clean(self):
        # Don't allow a bill of materials to contain itself.
        if self.bom.product == self.product:
            raise ValidationError(_("BOM inceptions are not advisable."))


class Location(models.Model):
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, related_name="warehouse_locations"
    )
    product = models.ManyToManyField(Product, related_name="product_locations")
    name = models.CharField(max_length=128)

    class Meta:
        unique_together = ("warehouse", "name")

    def __str__(self):
        return self.name
