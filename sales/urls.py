from django.urls import path
from .views import (
    CustomerCreate,
    CustomerDetail,
    CustomerList,
    ShipmentSchedule,
    ShipmentDetail,
)

urlpatterns = [
    path("customers/", CustomerList.as_view(), name="customer_list"),
    path("customers/<int:pk>/", CustomerDetail.as_view(), name="customer_detail"),
    path("customers/create/", CustomerCreate.as_view(), name="customer_create"),
    path("shipments/", ShipmentSchedule.as_view(), name="shipment_schedule"),
    path("shipments/<int:pk>/", ShipmentDetail.as_view(), name="shipment_detail"),
]
