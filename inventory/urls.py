from django.urls import path
from django.views.generic import TemplateView
from .views import ProductList

urlpatterns = [
    path(
        "dashboard/",
        TemplateView.as_view(template_name="inventory/index.html"),
        name="inventory_dashboard",
    ),
    path("products/", ProductList.as_view(), name="product_list"),
]
