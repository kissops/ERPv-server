from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"inventory", views.InventoryLedgerViewSet)
router.register(r"manufacturing", views.ManufacturingLedgerViewSet)
router.register(r"purchase", views.PurchaseLedgerViewSet)
router.register(r"sales", views.SalesLedgerViewSet)

urlpatterns = [path("", include(router.urls))]
