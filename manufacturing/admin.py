from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "quantity", "priority", "complete"]
    list_filter = ["complete", "priority"]
    search_fields = ["product"]
    list_per_page = 10

