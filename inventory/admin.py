from django.contrib import admin
from .models import Product, BillOfMaterials, BOMItem, Location, Warehouse


class BOMItemInline(admin.TabularInline):
    model = BOMItem
    readonly_fields = ["cost"]
    fields = ["product", "quantity", "cost"]
    extra = 0


class WHLocationInline(admin.TabularInline):
    fields = ["name"]
    model = Location
    extra = 0


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    inlines = [WHLocationInline]
    list_display = ["name", "locations"]
    search_fields = ("name",)
    list_per_page = 10


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": (("name", "warehouse"), "product")}),)
    filter_horizontal = ["product"]
    list_display = ["name", "warehouse"]
    search_fields = ("name",)
    list_per_page = 10


@admin.register(BillOfMaterials)
class BillOfMaterialsAdmin(admin.ModelAdmin):
    readonly_fields = ["total_cost"]
    fields = ["product", "total_cost"]
    inlines = [BOMItemInline]
    list_per_page = 10
    search_fields = ("product__name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": (("name", "quantity"), ("desired_stock_level",))}),
        (
            "Product Inventory Detail",
            {
                "classes": ("wide",),
                "fields": (("planned", "purchased", "sold", "allocated_for_jobs"),),
            },
        ),
        ("Product Requirements", {"fields": ("required",)}),
    )
    readonly_fields = ["planned", "purchased", "sold", "required", "allocated_for_jobs"]
    list_display = ["name", "quantity"]
    search_fields = ("name",)
    list_per_page = 10
