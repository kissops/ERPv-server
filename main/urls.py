from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='ERPv')

urlpatterns = [
    path("", schema_view),
    path("api-auth/", include("rest_framework.urls")),
    path("inventory/", include("inventory.urls")),
    path("ledger/", include("ledger.urls")),
    path("manufacturing/", include("manufacturing.urls")),
    path("purchase/", include("purchase.urls")),
    path("sales/", include("sales.urls")),
]
