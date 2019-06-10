from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.urls import reverse
from inventory.models import Product
from ledger.models import SalesLedger, InventoryLedger


class Customer(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    postcode = models.CharField(max_length=7)
    phone = models.CharField(max_length=64, blank=True)
    email = models.CharField(max_length=128, blank=True)
    website = models.CharField(max_length=256, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # new
        return reverse("customer_detail", args=[str(self.id)])


class SoldProduct(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer_sold_products"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_sold_product"
    )
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def sold(self):
        try:
            orders = sum(
                [
                    order.quantity
                    for order in self.product_sales_orders.filter(complete=False)
                ]
            )
            return orders
        except:
            pass


class SalesOrder(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer_sales_orders"
    )
    ship_by = models.DateTimeField(blank=True, null=True)
    shipped_on = models.DateTimeField(blank=True, null=True)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ["ship_by"]

    def __str__(self):
        return f"{self.pk}"

    def value(self):
        return sum([line.value for line in self.sales_order_lines.all()])

    def shipped_value(self):
        return sum([line.shipped_value() for line in self.sales_order_lines.all()])

    def save(self, *args, **kwargs):
        if self.complete == True:
            SalesLedger.objects.create(
                name=self.pk, amount=0.00, value=self.shipped_value()
            )
        super().save(*args, **kwargs)


class SalesOrderLine(models.Model):
    sales_order = models.ForeignKey(
        SalesOrder, on_delete=models.CASCADE, related_name="sales_order_lines"
    )
    product = models.ForeignKey(
        SoldProduct, on_delete=models.CASCADE, related_name="product_sales_orders"
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    shipped_quantity = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    created_date = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)
    complete_date = models.DateTimeField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        ordering = ["product__name"]

    def save(self, *args, **kwargs):
        # set the value of the line if not set.
        if self.value != 0.00:
            pass
        else:
            self.value = self.valued()
        # if line is complete remove the product from inventory.
        if self.complete == True:
            product = Product.objects.get(pk=self.product.product.pk)
            product.quantity = product.quantity - Decimal(self.shipped_quantity)
            product.save()
            self.complete_date = timezone.now()
            # also create a ledger entry when shipping product
            if self.shipped_quantity != 0.00:
                InventoryLedger.objects.create(
                    name=self.product.product,
                    amount=self.shipped_quantity * -1,
                    value=self.shipped_value(),
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name

    def valued(self):
        try:
            v = Decimal(self.product.price) * Decimal(self.quantity)
        except:
            v = 0.00
        return v

    def shipped_value(self):
        try:
            sv = (
                Decimal(self.value)
                / Decimal(self.quantity)
                * Decimal(self.shipped_quantity)
            )
        except:
            sv = 0.00
        return round(sv, 2)
