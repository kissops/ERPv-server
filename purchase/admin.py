from django.contrib import admin
from .models import Supplier, PurchasedProduct, PurchaseOrder, PurchaseOrderLine


class PurchaseOrderInline(admin.TabularInline):
    model = PurchaseOrderLine
    readonly_fields = ["value", "received_value"]
    fields = [
        "product",
        "quantity",
        "value",
        "received_quantity",
        "received_value",
        "complete",
    ]
    extra = 0


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ["id", "supplier", "due_by", "value"]
    list_filter = ["due_by"]
    inlines = [PurchaseOrderInline]
    search_fields = ["id", "supplier__name"]
    list_per_page = 10


class PurchasedProductInline(admin.TabularInline):
    readonly_fields = ["on_order"]
    model = PurchasedProduct
    extra = 0


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    inlines = [PurchasedProductInline]
    list_per_page = 10
    search_fields = ("name",)
