from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"customers", views.CustomerViewSet)
router.register(r"sold_products", views.SoldProductViewSet)
router.register(r"sales_orders", views.SalesOrderViewSet)
router.register(r"sales_order_lines", views.SalesOrderLineViewSet)

urlpatterns = [path("", include(router.urls))]
