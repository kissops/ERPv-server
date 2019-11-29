from rest_framework import serializers
from .models import Customer, CustomerContact, SoldProduct, SalesOrder, SalesOrderLine


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
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


class CustomerContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerContact
        fields = ["url", "id", "customer", "first_name", "last_name"]


class SoldProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoldProduct
        fields = ["url", "id", "customer", "product", "name", "price"]


class SalesOrderSerializer(serializers.HyperlinkedModelSerializer):
    sales_order_lines = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="salesorderline-detail"
    )

    class Meta:
        model = SalesOrder
        fields = [
            "url",
            "id",
            "customer",
            "shipped_on",
            "complete",
            "value",
            "shipped_value",
            "sales_order_lines",
        ]


class SalesOrderLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SalesOrderLine
        fields = [
            "url",
            "id",
            "sales_order",
            "product",
            "quantity",
            "shipped_quantity",
            "created_date",
            "complete",
            "complete_date",
            "value",
            "shipped_value",
        ]
