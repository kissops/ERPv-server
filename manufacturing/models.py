from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from inventory.models import Product
from ledger.models import ManufacturingLedger, InventoryLedger
from statistics import mean


class BillOfMaterials(models.Model):
    """
    This is the products Bill of Materials.
    ie: an intermediate object to the list of BOMitems that make up the product.
    """

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    labour_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        ordering = ["product"]
        verbose_name_plural = "Bill of Materials"

    def __str__(self):
        return self.product.name

    def total_cost(self):
        try:
            tc = (
                sum([bom_line.cost() for bom_line in self.bom_items.all()])
                + self.labour_cost
            )
            return tc
        except:
            return sum([bom_line.cost() for bom_line in self.bom_items.all()])


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

    def cost(self):
        # return an average of all purchased product costs.
        average = mean(p.cost for p in self.product.product_purchased_product.all())
        return average * Decimal(self.quantity)


class Job(models.Model):
    """
    Job model: 
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_jobs"
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    priority = models.IntegerField(default=2)
    created_date = models.DateTimeField(default=timezone.now)
    bom_allocated = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    complete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["priority"]

    def bom(self):
        try:
            bom = [
                item
                for item in self.product.billofmaterials.bom_items.all().prefetch_related(
                    "product"
                )
            ]
            return bom
        except:
            pass

    def save(self, *args, **kwargs):
        if self.complete == True and self.bom_allocated == True:
            product = Product.objects.get(pk=self.product.pk)
            product.quantity = product.quantity + Decimal(self.quantity)
            product.save()
            if self.quantity != 0.00:
                ManufacturingLedger.objects.create(
                    name=self.product, amount=self.quantity, value=0.00
                )
                InventoryLedger.objects.create(
                    name=self.product, amount=self.quantity, value=0.00
                )
            self.complete_date = timezone.now()
            if self.bom() is not None:
                for item in self.bom():
                    product = Product.objects.get(pk=item.product.pk)
                    product.quantity = product.quantity - item.quantity * Decimal(
                        self.quantity
                    )
                    product.allocated_for_jobs = (
                        product.allocated_for_jobs
                        - item.quantity * Decimal(self.quantity)
                    )
                    product.save()
                    if product.quantity != 0.00:
                        InventoryLedger.objects.create(
                            name=product.name, amount=product.quantity, value=0.00
                        )
        else:
            if self.bom() is not None:
                for item in self.bom():
                    product = Product.objects.get(pk=item.product.pk)
                    product.allocated_for_jobs = (
                        product.allocated_for_jobs
                        + item.quantity * Decimal(self.quantity)
                    )
                    product.save()
                self.bom_allocated = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name
