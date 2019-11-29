from rest_framework import serializers
from .models import (
    Supplier,
    SupplierContact,
    PurchasedProduct,
    PurchaseOrder,
    PurchaseOrderLine,
)


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


class SupplierContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SupplierContact
        fields = ["url", "id", "supplier", "first_name", "last_name"]


class PurchasedProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchasedProduct
        fields = ["url", "id", "supplier", "product", "name", "cost", "on_order"]


class PurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
    purchase_order_lines = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="purchaseorderline-detail"
    )

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
            "purchase_order_lines",
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
