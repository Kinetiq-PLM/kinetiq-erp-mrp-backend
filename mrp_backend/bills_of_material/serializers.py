from rest_framework import serializers
from .models import BillOfMaterials

class BillOfMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillOfMaterials
        fields = [
            "bom_id",
            "product_id",
            "quantity_of_product",
            "material_id",
            "quantity_of_material",
            "product_description",
            "specific_notes",
            "production_order_detail_id",
            "cost_per_raw_material",
            "total_cost_of_raw_materials",
            "cost_of_production",
            "labor_cost",
            "total_cost"
        ]