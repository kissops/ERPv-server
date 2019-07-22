from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"suppliers", views.SupplierViewSet)
router.register(r"purchased_products", views.PurchasedProductViewSet)
router.register(r"purchase_orders", views.PurchaseOrderViewSet)
router.register(r"purchase_order_lines", views.PurchaseOrderLineViewSet)

urlpatterns = [path("", include(router.urls))]
