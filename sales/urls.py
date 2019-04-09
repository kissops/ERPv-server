from django.urls import path
from .views import ShipmentSchedule, ShipmentDetail

urlpatterns = [
    path("shipments/", ShipmentSchedule.as_view(), name="shipment_schedule"),
    path("shipments/<int:pk>/", ShipmentDetail.as_view(), name="shipment_detail"),
]
