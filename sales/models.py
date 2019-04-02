from decimal import Decimal
from django.db import models
from django.utils import timezone
from inventory.models import Product


class Customer(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    postcode = models.CharField(max_length=7)
    phone = models.CharField(max_length=64, blank=True)
    email = models.CharField(max_length=128, blank=True)
    website = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name


class SoldProduct(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer_sold_products"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_sold_product"
    )
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)

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

    def __str__(self):
        return f"{self.pk}"

    def value(self):
        return sum([line.value() for line in self.sales_order_lines.all()])


class SalesOrderLine(models.Model):
    sales_order = models.ForeignKey(
        SalesOrder, on_delete=models.CASCADE, related_name="sales_order_lines"
    )
    product = models.ForeignKey(
        SoldProduct, on_delete=models.CASCADE, related_name="product_sales_orders"
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    created_date = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)
    complete_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.complete == True:
            product = Product.objects.get(pk=self.product.product.pk)
            product.quantity = product.quantity - Decimal(self.quantity)
            product.save()
            self.complete_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name

    def value(self):
        return Decimal(self.product.price) * Decimal(self.quantity)
