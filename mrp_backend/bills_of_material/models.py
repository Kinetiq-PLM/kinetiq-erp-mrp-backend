from django.db import models
import datetime
from connected_modules.admin.models import Products,RawMaterials,ItemMasterData
from connected_modules.production.models import ProductionOrdersDetails, Labor, ProductionOrdersHeader
from connected_modules.sales.models import Orders, ProductPricing, StatementItem
from connected_modules.project_management.models import ExternalProjectDetails
from connected_modules.human_resources.models import EmployeeSalary
from connected_modules.services.models import ServiceOrderItem
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
    production_order_detail_id = models.CharField(
        db_column='production_order_detail_id',
    )
    labor_cost_id = models.CharField(
        db_column='labor_cost_id',
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
    final_price = models.DecimalField(
        db_column='final_price',
        max_digits=10,
        decimal_places=2
    )
    statement_item_id = models.CharField(
        db_column='statement_item_id'
    )

    class Meta:
        managed = False
        db_table = 'non_project_order_pricing'


class PrincipalItems(models.Model):
    principal_item_id = models.CharField(
        db_column='principal_item_id',
        primary_key=True,
        max_length=255
    )
    service_order_item_id = models.CharField(
        db_column='service_order_item_id',
    )
    item_id = models.CharField(
        db_column='item_id',
    )
    mark_up_price = models.DecimalField(
        db_column='mark_up_price',
        max_digits=10,
        decimal_places=2
    )
    class Meta:
        managed = False
        db_table = 'principal_items'

class ProductRawMaterialCost(models.Model):
    product = models.CharField(
        db_column='product', 
        primary_key=True,
        max_length=255
    )
    quantity_of_product = models.IntegerField(
        db_column='quantity_of_product'
    )
    raw_material = models.CharField(
        db_column='raw_material',
        max_length=255
    )
    quantity_of_raw_material = models.DecimalField(
        db_column='quantity_of_raw_material',
        max_digits=10,
        decimal_places=2
    )
    unit_of_measure = models.CharField(
        db_column='unit_of_measure',
        default='unit'
    )
    cost_per_raw_material = models.DecimalField(
        db_column='cost_per_raw_material',
        max_digits=10,
        decimal_places=2
    )
    total_cost_of_raw_materials = models.DecimalField(
        db_column='total_cost_of_raw_materials',
        max_digits=10,
        decimal_places=2
    )
    
    class Meta:
        managed = False
        db_table = 'product_raw_material_costs'


class BOMList(models.Model):
    bom_no = models.CharField(
        db_column='BOM No.',
        primary_key=True,
        max_length=255
    )
    type = models.TextField(
        db_column='Type'
    )
    status = models.TextField(
        db_column='Status'
    )
    date_created = models.DateTimeField(
        db_column='Date Created'
    )

    class Meta:
        managed = False
        db_table = 'bom_list'

class OrderList(models.Model):
    order_no = models.CharField(
        db_column='Order No.',
        primary_key=True,
        max_length=255
    )
    type = models.TextField(
        db_column='Type'
    )
    details = models.TextField(
        db_column='Details'
    )
    date = models.DateField(
        db_column='Date'
    )

    class Meta:
        managed = False
        db_table = 'order_list'

class ProductPricing(models.Model):
    statement_id = models.CharField(
        db_column='statement_id',
        primary_key=True,
        max_length=255
    )
    statement_item_id = models.CharField(
        db_column='statement_item_id'
    )
    product_id = models.CharField(
        db_column='Product ID'
    )
    product_name = models.TextField(
        db_column='Product'
    )
    product_description = models.TextField(
        db_column='Product Description'
    )
    quantity = models.IntegerField(
        db_column='Quantity'
    )
    cost = models.DecimalField(
        db_column='Total Product Cost',
        max_digits=10,
        decimal_places=2
    )
    class Meta:
        managed = False
        db_table = 'product_pricing'


class CostOfRawMaterials(models.Model):
    product_id = models.CharField(
        db_column='product_id',
        primary_key=True,
        max_length=255
    )
    raw_material = models.CharField(
        db_column='Raw Material'
    )
    material_id = models.CharField(
        db_column='Material ID'
    )
    rm_quantity = models.DecimalField(
        db_column='RM Quantity',
        max_digits=10,
        decimal_places=2
    )
    units = models.CharField(
        db_column='Units'
    )
    unit_cost = models.DecimalField(
        db_column='Unit Cost',
        max_digits=10,
        decimal_places=2
    )
    total_cost = models.DecimalField(
        db_column='Total Cost',
        max_digits=10,
        decimal_places=2
    )
    class Meta:
        managed = False
        db_table = 'cost_of_materials'

class OrderProductionCosts(models.Model):
    order_id = models.CharField(
        db_column='order_id',
        primary_key=True,
        max_length=255
    )
    ext_project_request_id = models.CharField(
        db_column='ext_project_request_id'
    )
    project_id = models.CharField(
        db_column='project_id'
    )
    task_id = models.CharField(
        db_column='task_id'
    )
    production_order_id = models.CharField(
        db_column='production_order_id'
    )
    production_order_detail_id = models.CharField(
        db_column='production_order_detail_id'
    )
    cost_of_production = models.DecimalField(
        db_column='cost_of_production',
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        managed = False
        db_table = 'order_production_costs'

class EmployeeOrder(models.Model):
    order_id = models.CharField(
        db_column='order_id',
        primary_key=True,
        max_length=255
    )
    ext_project_request_id = models.CharField(
        db_column='ext_project_request_id'
    )
    project_id = models.CharField(
        db_column='project_id'
    )
    task_id = models.CharField(
        db_column='task_id'
    )
    production_order_id = models.CharField(
        db_column='production_order_id'
    )
    employee_id = models.CharField(
        db_column='employee_id'
    )
    labor_cost_id = models.CharField(
        db_column='labor_cost_id'
    )
    days_worked = models.IntegerField(
        db_column='days_worked'
    )
    daily_rate = models.DecimalField(
        db_column='daily_rate',
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        managed = False
        db_table = 'employee_order'

class NonProjectProductCost(models.Model):
    statement_id = models.CharField(
        db_column='statement_id',
        primary_key=True,
        max_length=255
    )
    statement_item_id = models.CharField(
        db_column='statement_item_id'
    )
    product_id = models.CharField(
        db_column='item_id'
    )
    product_name = models.TextField(
        db_column='item_name'
    )
    description = models.TextField(
        db_column='item_description'
    )
    quantity = models.IntegerField(
        db_column='quantity'
    )
    item_price = models.DecimalField(
        db_column='item_price',
        max_digits=10,
        decimal_places=2
    )
    product_cost = models.DecimalField(
        db_column='Product Cost',
        max_digits=10,
        decimal_places=2
    )
    class Meta:
        managed = False
        db_table = 'np_product_cost'


class ProjectBOMDetail(models.Model):
    statement_id = models.CharField(
        db_column='statement_id',
        primary_key=True,
        max_length=255
    )
    statement_item_id = models.CharField(
        db_column='statement_item_id'
    )
    product_name = models.TextField(
        db_column='Product'
    )
    qty_of_product = models.IntegerField(
        db_column='Qty. Of Product'
    )
    raw_material_name = models.TextField(
        db_column='Raw Material'
    )
    qty_of_raw_material = models.DecimalField(
        db_column='Qty. Of Raw Material',
        max_digits=10,
        decimal_places=2
    )
    units = models.CharField(
        db_column='Units'
    )
    cost_per_rm = models.DecimalField(
        db_column='Cost Per Raw Material',
        max_digits=10,
        decimal_places=2
    )
    total_cost_per_rm = models.DecimalField(
        db_column='Total Cost Per Raw Material',
        max_digits=10,
        decimal_places=2
    )
    class Meta:
        managed = False
        db_table = 'project_bom_detail'

class NonProjectBOMDetail(models.Model):
    statement_id = models.CharField(
        db_column='statement_id',
        primary_key=True,
        max_length=255
    )
    product_id = models.CharField(
        db_column='item_id'
    )
    product_name = models.TextField(
        db_column='item_name'
    )
    quantity = models.IntegerField(
        db_column='quantity'
    )
    unit_of_measure = models.CharField(
        db_column='unit_of_measure'
    )
    selling_price = models.DecimalField(
        db_column='item_price',
        max_digits=10,
        decimal_places=2
    )
    product_cost = models.DecimalField(
        db_column='Product Cost',
        max_digits=10,
        decimal_places=2
    )
    class Meta:
        managed = False
        db_table = 'np_bom_detail'


class PrincipalBOMDetail(models.Model):
    service_order_id = models.CharField(
        db_column='service_order_id',
        primary_key=True,
        max_length=255
    )
    service_order_item_id = models.CharField(
        db_column='service_order_item_id',
    )
    item_name = models.TextField(
        db_column='item_name'
    )
    item_quantity = models.IntegerField(
        db_column='item_quantity'
    )
    unit_of_measure = models.CharField(
        db_column='unit_of_measure'
    )
    item_price = models.DecimalField(
        db_column='item_price',
        max_digits=10,
        decimal_places=2
    )
    total_item_price = models.DecimalField(
        db_column='total_item_price',
        max_digits=10,
        decimal_places=2
    )
    class Meta:
        managed = False
        db_table = 'principal_bom_detail'

class PrincipalItemOrderList(models.Model):
    service_order_id = models.CharField(
        db_column='service_order_id',
        primary_key=True,
        max_length=255
    )
    type = models.TextField(
        db_column='type'
    )
    description = models.TextField(
        db_column='description_details'
    )
    date = models.DateTimeField(
        db_column='date'
    )
    class Meta:
        managed = False
        db_table = 'principal_item_orders'

class PrincipalOrderItem(models.Model):
    service_order_id = models.CharField(
        db_column='service_order_id',
        primary_key=True,
        max_length=255
    )
    service_order_item_id = models.CharField(
        db_column='service_order_item_id'
    )
    item_id = models.CharField(
        db_column='item_id'
    )
    item_name = models.TextField(
        db_column='item_name'
    )
    item_quantity = models.IntegerField(
        db_column='item_quantity'
    )
    unit_of_measure = models.CharField(
        db_column='unit_of_measure'
    )
    item_price = models.DecimalField(
        db_column='item_price',
        max_digits=10,
        decimal_places=2
    )
    total_item_price = models.DecimalField(
        db_column='total_item_price',
        max_digits=10,
        decimal_places=2
    )
    class Meta:
        managed = False
        db_table = 'principal_item_details'

class TrackingNpop(models.Model):
    tracking_npop_id = models.CharField(
        db_column='tracking_npop_id',
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
    status = models.CharField(
        db_column='status'
    )
    class Meta:
        managed = False
        db_table = 'tracking_npop'


class TrackingPrincipal(models.Model):
    tracking_principal_id = models.CharField(
        db_column='tracking_principal_id',
        primary_key=True,
        max_length=255
    )
    status = models.CharField(
        db_column='status'
    )
    service_order_id = models.CharField(
        db_column='service_order_id'
    )
    class Meta:
        managed = False
        db_table = 'tracking_principal'


class ProjectProductMats(models.Model):
    statement_id = models.CharField(
        db_column='statement_id',
        primary_key=True,
        max_length=255
    )
    product_mats_id = models.CharField(
        db_column='product_mats_id'
    )
    quantity_required = models.DecimalField(
        db_column='quantity_required',
        max_digits=10,
        decimal_places=2
    )
    cost_per_raw_material = models.DecimalField(
        db_column='cost_per_raw_material',
        max_digits=10,
        decimal_places=2
    )
    total_cost_of_raw_materials = models.DecimalField(
        db_column='total_cost_of_raw_materials',
        max_digits=10,
        decimal_places=2
    )
    class Meta:
        managed = False
        db_table = 'project_productmats'