from django.db import models
import datetime
from connected_modules.admin.models import Products,RawMaterials
from connected_modules.production.models import ProductionOrdersDetails, Labor
from connected_modules.sales.models import Orders
from connected_modules.project_management.models import ExternalProjectDetails
from connected_modules.human_resources.models import EmployeeSalary
from django.utils.translation import gettext as _

class ProductMats(models.Model):
    product_mats_id = models.CharField(
        db_column='product_mats_id',
        primary_key=True,
        max_length=255
    )
    product_id = models.ForeignKey(
        Products,
        db_column='product_id',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    material_id = models.ForeignKey(
        RawMaterials,
        db_column='material_id',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    quantity_required = models.DecimalField(
        db_column='quantity_required',
        max_digits=10,
        decimal_places=2,
        null=False
    )
    cost_of_used_materials = models.DecimalField(
        db_column='cost_of_used_materials',
        max_digits=10,
        decimal_places=2,
        null=False
    )

    class Meta:
        managed = False
        db_table = 'product_mats'

class LaborCost(models.Model):
    labor_cost_id = models.CharField(
        db_column='labor_cost_id',
        primary_key=True,
        max_length=255
    )
    labor_id = models.ForeignKey(
        Labor,
        db_column='labor_id',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    salary_id = models.ForeignKey(
        EmployeeSalary,
        db_column='salary_id',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'labor_cost'

class BillOfMaterials(models.Model):
    bom_id = models.CharField(
        db_column='bom_id',
        primary_key=True,
        max_length=255
    )
    project_id = models.ForeignKey(
        ExternalProjectDetails,
        db_column='project_id',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    product_mats_id = models.ForeignKey(
        ProductMats,
        db_column='product_mats_id',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    overall_quantity_of_material = models.IntegerField(
        db_column='overall_quantity_of_material',
        null=True
    )
    cost_per_raw_material = models.DecimalField(
        db_column='cost_per_raw_material',
        max_digits=10,
        decimal_places=2,
        null=False
    )
    total_cost_of_raw_materials = models.DecimalField(
        db_column='total_cost_of_raw_materials',
        max_digits=10,
        decimal_places=2,
        null=False
    )
    production_order_detail_id = models.ForeignKey(
        ProductionOrdersDetails,
        db_column='production_order_detail_id',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    labor_cost_id = models.ForeignKey(
        LaborCost,
        db_column='labor_cost_id',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    total_cost = models.DecimalField(
        db_column='total_cost',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    class Meta:
        managed = False
        db_table = 'bill_of_materials'

class NonProjectOrderPricing(models.Model):
    non_project_costing_id = models.CharField(
        db_column='non_project_costing_id',
        primary_key=True,
        max_length=255
    )
    order_id = models.ForeignKey(
        Orders,
        db_column='order_id',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    final_price = models.DecimalField(
        db_column='final_price',
        max_digits=10,
        decimal_places=2,
        null=False,
    )

    class Meta:
        managed = False
        db_table = 'non_project_order_pricing'


