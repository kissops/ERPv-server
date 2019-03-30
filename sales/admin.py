from django.contrib import admin
from .models import Customer, SoldProduct, SalesOrder, SalesOrderLine


class SalesOrderInline(admin.TabularInline):
    model = SalesOrderLine
    extra = 0


@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "ship_by"]
    list_filter = ["ship_by"]
    inlines = [SalesOrderInline]
    search_fields = ["id", "customer__name"]
    list_per_page = 10


class SoldProductInline(admin.TabularInline):
    model = SoldProduct
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [SoldProductInline]
    list_per_page = 10
    search_fields = ("name",)
