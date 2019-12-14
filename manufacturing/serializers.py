from rest_framework import serializers
from .models import BillOfMaterials, BOMItem, Job


class BillOfMaterialsSerializer(serializers.HyperlinkedModelSerializer):
    bom_items = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="bomitem-detail"
    )

    class Meta:
        model = BillOfMaterials
        fields = ["url", "id", "product", "labour_cost", "total_cost", "bom_items"]


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
            "product_name",
            "quantity",
            "priority",
            "created_date",
            "bom_allocated",
            "complete",
            "complete_date",
        ]

    product_name = serializers.SerializerMethodField("get_product_name")

    def get_product_name(self, obj):
        return obj.product.name
