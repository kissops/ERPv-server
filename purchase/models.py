from decimal import Decimal
from django.db import models
from django.utils import timezone
from inventory.models import Product
from ledger.models import PurchaseLedger, InventoryLedger


class Supplier(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    postcode = models.CharField(max_length=7)
    phone = models.CharField(max_length=64, blank=True)
    email = models.CharField(max_length=128, blank=True)
    website = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name


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

    def on_order(self):
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


class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name="supplier_purchase_orders"
    )
    due_by = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["due_by"]

    def __str__(self):
        return f"{self.pk}"

    def value(self):
        return sum([line.value() for line in self.purchase_order_lines.all()])

    def received_value(self):
        return sum([line.received_value() for line in self.purchase_order_lines.all()])

    def complete(self):
        return [line.complete for line in self.purchase_order_lines.all()]


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
    received_quantity = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    created_date = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)
    complete_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.complete == True:
            product = Product.objects.get(pk=self.product.product.pk)
            product.quantity = product.quantity + Decimal(self.received_quantity)
            product.save()
            self.complete_date = timezone.now()
            # create a ledger entry when receiving product
            InventoryLedger.objects.create(
                name=self.product.product,
                amount=self.received_quantity,
                value=self.received_value(),
            )
        super().save(*args, **kwargs)
        if self.complete == True:
            if False in [self.purchase_order.complete()]:
                pass
            else:
                if self.received_quantity != 0.00:
                    PurchaseLedger.objects.create(
                        name=self.purchase_order.supplier,
                        amount=0.00,
                        value=self.purchase_order.received_value(),
                    )

    def __str__(self):
        return self.product.name

    def value(self):
        return Decimal(self.product.cost) * Decimal(self.quantity)

    def received_value(self):
        return Decimal(self.product.cost) * Decimal(self.received_quantity)
