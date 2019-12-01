from .models import (
    Ledger,
    InventoryLedger,
    ManufacturingLedger,
    PurchaseLedger,
    SalesLedger,
)
from .serializers import (
    InventoryLedgerSerializer,
    ManufacturingLedgerSerializer,
    PurchaseLedgerSerializer,
    SalesLedgerSerializer,
)
from rest_framework import viewsets


class InventoryLedgerViewSet(viewsets.ModelViewSet):
    queryset = InventoryLedger.objects.all()
    serializer_class = InventoryLedgerSerializer


class ManufacturingLedgerViewSet(viewsets.ModelViewSet):
    queryset = ManufacturingLedger.objects.all()
    serializer_class = ManufacturingLedgerSerializer


class PurchaseLedgerViewSet(viewsets.ModelViewSet):
    queryset = PurchaseLedger.objects.all()
    serializer_class = PurchaseLedgerSerializer


class SalesLedgerViewSet(viewsets.ModelViewSet):
    queryset = SalesLedger.objects.all()
    serializer_class = SalesLedgerSerializer
