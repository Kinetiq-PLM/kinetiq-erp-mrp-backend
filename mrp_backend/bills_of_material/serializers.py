from rest_framework import serializers
from .models import BillOfMaterials, NonProjectOrderPricing, ProductMats, LaborCost, ProductRawMaterialCost, BOMList, OrderList, ProductPricing, CostOfRawMaterials, OrderProductionCosts, EmployeeOrder
from connected_modules.sales.models import Orders
from connected_modules.admin.models import Products

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

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderList
        fields = '__all__'

class ProductPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPricing
        fields = '__all__'

class CostOfRawMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostOfRawMaterials
        fields = '__all__'

class OrderStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = [
            "order_id",
            "statement_id",
            "ext_project_request_id"
        ]

class OrderProductionCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProductionCosts
        fields = '__all__'

class EmployeeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeOrder
        fields = '__all__'