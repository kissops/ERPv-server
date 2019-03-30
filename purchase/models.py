from decimal import Decimal
from django.db import models
from django.utils import timezone
from inventory.models import Product


class Supplier(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    postcode = models.CharField(max_length=7)
    phone = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    website = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name="supplier_purchase_orders"
    )
    due_by = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}"


class PurchasedProduct(models.Model):
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name="supplier_products"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_purchased_product"
    )
    name = models.CharField(max_length=128)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def purchased(self):
        try:
            orders = sum(
                [
                    order.quantity
                    for order in self.product_purchase_orders.filter(complete=False)
                ]
            )
            return orders
        except:
            pass


class PurchaseOrderLine(models.Model):
    purchase_order = models.ForeignKey(
        PurchaseOrder, on_delete=models.CASCADE, related_name="purchase_order_lines"
    )
    product = models.ForeignKey(
        PurchasedProduct,
        on_delete=models.CASCADE,
        related_name="product_purchase_orders",
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    created_date = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)
    complete_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.complete == True:
            product = Product.objects.get(pk=self.product.product.pk)
            product.quantity = product.quantity + Decimal(self.quantity)
            product.save()
            self.complete_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name
