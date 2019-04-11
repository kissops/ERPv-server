from django.contrib import admin
from .models import InventoryLedger, ManufacturingLedger, PurchaseLedger, SalesLedger


@admin.register(InventoryLedger)
class InventoryLedgerAdmin(admin.ModelAdmin):
    list_display = ["name", "amount", "value", "date"]


@admin.register(ManufacturingLedger)
class ManufacturingLedgerAdmin(admin.ModelAdmin):
    list_display = ["name", "amount", "value", "date"]


@admin.register(PurchaseLedger)
class PurchaseLedgerAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "date"]


@admin.register(SalesLedger)
class SalesLedgerAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "date"]
