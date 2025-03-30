from django.db import models
import datetime
from connected_modules.admin.models import Products,RawMaterials
from connected_modules.production.models import ProductionOrdersDetails
from django.utils.translation import gettext as _

class BillOfMaterials(models.Model):
    bom_id = models.CharField(
        db_column='bom_id',
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
    quantity_of_product = models.IntegerField(
        db_column='quantity_of_product',
        null=True
    )
    material_id = models.ForeignKey(
        RawMaterials,
        db_column='material_id',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    quantity_of_material = models.IntegerField(
        db_column='quantity_of_material',
        null=True
    )
    product_description = models.TextField(
        db_column='product_description',
        null=True,
        blank=True
    )
    specific_notes = models.TextField(
        db_column='specific_notes',
        null=True,
        blank=True
    )
    production_order_detail_id = models.ForeignKey(
        ProductionOrdersDetails,
        db_column='production_order_detail_id',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
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
    cost_of_production = models.DecimalField(
        db_column='cost_of_production',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    labor_cost = models.DecimalField(
        db_column='labor_cost',
        max_digits=10,
        decimal_places=2,
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