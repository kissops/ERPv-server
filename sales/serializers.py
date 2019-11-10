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
        fields = ["url", "id", "customer", "product", "name", "sold"]


class SalesOrderSerializer(serializers.HyperlinkedModelSerializer):
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
