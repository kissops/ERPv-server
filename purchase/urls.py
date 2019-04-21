from django.urls import path
from .views import (
    DeliverySchedule,
    DeliveryDetail,
    PurchaseOrderCreate,
    SupplierCreate,
    SupplierDetail,
    SupplierUpdate,
    SupplierList,
)

urlpatterns = [
    path("deliveries/", DeliverySchedule.as_view(), name="delivery_schedule"),
    path("deliveries/<int:pk>/", DeliveryDetail.as_view(), name="delivery_detail"),
    path("suppliers/", SupplierList.as_view(), name="supplier_list"),
    path("suppliers/<int:pk>/", SupplierDetail.as_view(), name="supplier_detail"),
    path(
        "suppliers/<int:pk>/purchase_order/create/",
        PurchaseOrderCreate.as_view(),
        name="purchase_order_create",
    ),
    path(
        "suppliers/<int:pk>/update/", SupplierUpdate.as_view(), name="supplier_update"
    ),
    path("suppliers/create/", SupplierCreate.as_view(), name="supplier_create"),
]
