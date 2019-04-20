from django.urls import path
from django.views.generic import TemplateView
from .views import (
    ProductList,
    ProductDetail,
    WarehouseCreate,
    WarehouseList,
    WarehouseDetail,
    LocationList,
    LocationDetail,
)

urlpatterns = [
    path(
        "dashboard/",
        TemplateView.as_view(template_name="inventory/index.html"),
        name="inventory_dashboard",
    ),
    path("products/", ProductList.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("warehouses/", WarehouseList.as_view(), name="warehouse_list"),
    path("warehouses/<int:pk>/", WarehouseDetail.as_view(), name="warehouse_detail"),
    path("warehouses/create/", WarehouseCreate.as_view(), name="warehouse_create"),
    path("locations/", LocationList.as_view(), name="location_list"),
    path("locations/<int:pk>/", LocationDetail.as_view(), name="location_detail"),
]
