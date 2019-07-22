from rest_framework import serializers
from .models import Supplier, PurchasedProduct, PurchaseOrder, PurchaseOrderLine


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            "url",
            "id",
            "name",
            "address",
            "postcode",
            "phone",
            "email",
            "website",
        ]


class PurchasedProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchasedProduct
        fields = ["url", "id", "supplier", "product", "name", "cost", "on_order"]


class PurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = [
            "url",
            "id",
            "supplier",
            "due_by",
            "received_on",
            "complete",
            "value",
            "received_value",
        ]


class PurchaseOrderLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseOrderLine
        fields = [
            "url",
            "id",
            "purchase_order",
            "product",
            "quantity",
            "received_quantity",
            "created_date",
            "complete",
            "complete_date",
            "value",
            "received_value",
        ]
