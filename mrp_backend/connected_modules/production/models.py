# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Equipment(models.Model):
    equipment_id = models.CharField(primary_key=True, max_length=255)
    equipment_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    availability_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_maintenance_date = models.DateField(blank=True, null=True)
    equipment_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'equipment'


class Labor(models.Model):
    labor_id = models.CharField(primary_key=True, max_length=255)
    production_order = models.ForeignKey('ProductionOrdersHeader', models.DO_NOTHING, blank=True, null=True)
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    date_worked = models.DateTimeField(blank=True, null=True)
    days_worked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'labor'


class ProductionOrdersDetails(models.Model):
    production_order_detail_id = models.CharField(primary_key=True, max_length=255)
    production_order = models.ForeignKey('ProductionOrdersHeader', models.DO_NOTHING, blank=True, null=True)
    actual_quantity = models.IntegerField()
    cost_of_production = models.DecimalField(max_digits=10, decimal_places=2)
    miscellaneous_costs = models.DecimalField(max_digits=10, decimal_places=2)
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING, blank=True, null=True)
    rework_required = models.BooleanField()
    rework_notes = models.TextField(blank=True, null=True)
    external_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_orders_details'


class ProductionOrdersHeader(models.Model):
    production_order_id = models.CharField(primary_key=True, max_length=255)
    task_id = models.CharField(max_length=255, blank=True, null=True)
    bom_id = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_quantity = models.IntegerField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_orders_header'


class ProjectEquipment(models.Model):
    project_equipment_id = models.CharField(primary_key=True, max_length=255)
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING, blank=True, null=True)
    product_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_equipment'


class ReworkCost(models.Model):
    rework_cost_id = models.CharField(primary_key=True, max_length=255)
    production_order = models.ForeignKey(ProductionOrdersHeader, models.DO_NOTHING, blank=True, null=True)
    additional_cost = models.DecimalField(max_digits=10, decimal_places=2)
    additional_misc = models.DecimalField(max_digits=10, decimal_places=2)
    total_rework_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'rework_cost'
