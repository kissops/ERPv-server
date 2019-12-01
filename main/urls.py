from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ERPv",
        default_version="v0.1",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api-auth/", include("rest_framework.urls")),
    path("inventory/", include("inventory.urls")),
    path("ledger/", include("ledger.urls")),
    path("manufacturing/", include("manufacturing.urls")),
    path("purchase/", include("purchase.urls")),
    path("sales/", include("sales.urls")),
]
