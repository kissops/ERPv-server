from django.urls import path
from django.views.generic import TemplateView
from .views import ProductList, ReportList

urlpatterns = [
    path(
        "deliveries/",
        TemplateView.as_view(template_name="dashboards/deliveries.html"),
        name="deliveries",
    ),
    path(
        "jobs/", TemplateView.as_view(template_name="dashboards/jobs.html"), name="jobs"
    ),
    path("products/", ProductList.as_view(), name="products"),
    path("reports/", ReportList.as_view(), name="reports"),
    path(
        "shipments/",
        TemplateView.as_view(template_name="dashboards/shipments.html"),
        name="shipments",
    ),
]
