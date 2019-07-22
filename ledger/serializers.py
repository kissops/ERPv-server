from rest_framework import serializers
from .models import (
    Ledger,
    InventoryLedger,
    ManufacturingLedger,
    PurchaseLedger,
    SalesLedger,
)


class LedgerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ["url", "id", "name", "amount", "value", "date"]
        abstract = True


class InventoryLedgerSerializer(LedgerSerializer):
    class Meta:
        model = InventoryLedger
        fields = ["url", "id", "name", "amount", "value", "date"]


class ManufacturingLedgerSerializer(LedgerSerializer):
    class Meta:
        model = ManufacturingLedger
        fields = ["url", "id", "name", "amount", "value", "date"]


class PurchaseLedgerSerializer(LedgerSerializer):
    class Meta:
        model = PurchaseLedger
        fields = ["url", "id", "name", "amount", "value", "date"]


class SalesLedgerSerializer(LedgerSerializer):
    class Meta:
        model = SalesLedger
        fields = ["url", "id", "name", "amount", "value", "date"]
