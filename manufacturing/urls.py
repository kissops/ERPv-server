from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"bill_of_materials", views.BillOfMaterialsViewSet)
router.register(r"bom_items", views.BOMItemViewSet)
router.register(r"jobs", views.JobViewSet)

urlpatterns = [path("", include(router.urls))]
