from decimal import Decimal
from django.db import models
from django.utils import timezone
from inventory.models import Product


class Job(models.Model):
    """
    Job model: 
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_jobs"
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    priority = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
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
        if self.complete == True:
            product = Product.objects.get(pk=self.product.pk)
            product.quantity = product.quantity + Decimal(self.quantity)
            product.save()
            self.complete_date = timezone.now()
            if self.bom() is not None:
                for item in self.bom():
                    product = Product.objects.get(pk=item.product.pk)
                    product.quantity = product.quantity - item.quantity * self.quantity
                    product.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name
