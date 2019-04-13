from django.urls import path
from .views import (
    DeliverySchedule,
    DeliveryDetail,
    SupplierCreate,
    SupplierDetail,
    SupplierList,
)

urlpatterns = [
    path("deliveries/", DeliverySchedule.as_view(), name="delivery_schedule"),
    path("deliveries/<int:pk>/", DeliveryDetail.as_view(), name="delivery_detail"),
    path("suppliers/", SupplierList.as_view(), name="supplier_list"),
    path("suppliers/<int:pk>/", SupplierDetail.as_view(), name="supplier_detail"),
    path("suppliers/create/", SupplierCreate.as_view(), name="supplier_create"),
]
