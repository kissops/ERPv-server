from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"warehouses", views.WarehouseViewSet)
router.register(r"products", views.ProductViewSet)
router.register(r"locations", views.LocationViewSet)

urlpatterns = [path("", include(router.urls))]
