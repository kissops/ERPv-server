from rest_framework import serializers
from .models import BillOfMaterials, BOMItem, Job


class BillOfMaterialsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BillOfMaterials
        fields = ["url", "id", "product", "labour_cost", "total_cost"]


class BOMItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BOMItem
        fields = ["url", "id", "bom", "product", "quantity", "cost"]


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = [
            "url",
            "id",
            "product",
            "quantity",
            "priority",
            "created_date",
            "bom_allocated",
            "complete",
            "complete_date",
            "bom",
        ]
