from django.db import models
from django.utils import timezone


class Ledger(models.Model):
    name = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-date"]
        abstract = True


class InventoryLedger(Ledger):
    class Meta(Ledger.Meta):
        verbose_name_plural = "Inventory ledger"

    def __str__(self):
        return f"{self.pk}"


class ManufacturingLedger(Ledger):
    class Meta(Ledger.Meta):
        verbose_name_plural = "Manufacturing ledger"

    def __str__(self):
        return f"{self.pk}"


class PurchaseLedger(Ledger):
    class Meta(Ledger.Meta):
        verbose_name_plural = "Purchase ledger"

    def __str__(self):
        return f"{self.pk}"


class SalesLedger(Ledger):
    class Meta(Ledger.Meta):
        verbose_name_plural = "Sales ledger"

    def __str__(self):
        return f"{self.pk}"
