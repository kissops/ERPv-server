from rest_framework import serializers
from .models import Warehouse, Product, Location


class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Warehouse
        fields = ["url", "id", "name", "locations"]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            "url",
            "id",
            "name",
            "quantity",
            "allocated_for_jobs",
            "desired_stock_level",
            "planned",
            "purchased",
            "sold",
            "required",
        ]


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ["url", "id", "warehouse", "name"]
