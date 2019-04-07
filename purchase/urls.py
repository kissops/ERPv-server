from django.urls import path
from .views import DeliverySchedule, DeliveryDetail

urlpatterns = [
    path("deliveries/", DeliverySchedule.as_view(), name="delivery_schedule"),
    path("deliveries/<int:pk>/", DeliveryDetail.as_view(), name="delivery_detail"),
]

