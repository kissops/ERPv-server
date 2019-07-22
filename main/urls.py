from django.urls import path, include

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("inventory/", include("inventory.urls")),
    path("ledger/", include("ledger.urls")),
    path("manufacturing/", include("manufacturing.urls")),
    path("purchase/", include("purchase.urls")),
    path("sales/", include("sales.urls")),
]
