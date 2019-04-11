from django.contrib import admin
from .models import BillOfMaterials, BOMItem, Job


class BOMItemInline(admin.TabularInline):
    model = BOMItem
    readonly_fields = ["cost"]
    fields = ["product", "quantity", "cost"]
    extra = 0


@admin.register(BillOfMaterials)
class BillOfMaterialsAdmin(admin.ModelAdmin):
    readonly_fields = ["total_cost"]
    fields = ["product", "labour_cost", "total_cost"]
    inlines = [BOMItemInline]
    list_per_page = 10
    search_fields = ("product__name",)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    fields = ["product", "quantity", "priority", "complete"]
    list_display = ["id", "product", "quantity", "priority", "complete"]
    list_filter = ["complete", "priority"]
    search_fields = ["product"]
    list_per_page = 10
