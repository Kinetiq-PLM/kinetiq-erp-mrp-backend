from rest_framework import serializers
from .models import BillOfMaterials, NonProjectOrderPricing, ProductMats, LaborCost, ProductRawMaterialCost, BOMList

class BillOfMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillOfMaterials
        fields = [
            "bom_id",
            "project_id",
            "product_mats_id",
            "overall_quantity_of_material",
            "cost_per_raw_material",
            "total_cost_of_raw_materials",
            "production_order_detail_id",
            "labor_cost_id",
            "total_cost"
        ]

class NonProjectOrderPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonProjectOrderPricing
        fields = [
            "non_project_costing_id",
            "order_id",
            "final_price"
        ]

class ProductMatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMats
        fields = [
            "product_mats_id",
            "product_id",
            "material_id",
            "quantity_required",
            "cost_of_used_materials"
        ]

class LaborCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaborCost
        fields = [
            "labor_cost_id",
            "labor_id",
            "salary_id"
        ]

class ProductRawMaterialCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRawMaterialCost
        fields = '__all__'

class BOMListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMList
        fields = '__all__'