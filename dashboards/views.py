from django.views.generic import ListView
from inventory.models import Product
from report_builder.models import Report


class ProductList(ListView):
    model = Product
    template_name = "dashboards/products.html"


class ReportList(ListView):
    model = Report
    template_name = "dashboards/reports.html"
