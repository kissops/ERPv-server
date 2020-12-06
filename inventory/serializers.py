from rest_framework import serializers
from .models import Warehouse, Product, Location, LocationQuantity


class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    warehouse_locations = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="location-detail"
    )

    class Meta:
        model = Warehouse
        fields = ["url", "id", "name", "location_count", "warehouse_locations"]


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
        fields = ["url", "id", "warehouse", "name", "location_warehouse"]


class LocationQuantitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocationQuantity
        fields = [
            "url",
            "id",
            "product",
            "location",
            "quantity",
            "location_name",
            "location_warehouse",
            "product_name",
        ]
