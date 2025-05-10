from django.db import models

class ProductMaterial(models.Model):
    product_id = models.CharField(
        db_column='product_id',
        primary_key=True,
        max_length=255
    )
    item_name = models.CharField(
        db_column='item_name'
    )
    item_description = models.TextField(
        db_column='item_description'
    )
    class Meta:
        managed = False
        db_table = 'product_material'


class ProductRawMaterial(models.Model):
    product_id = models.CharField(
        db_column='product_id',
        primary_key=True,
        max_length=255
    )
    item_name = models.CharField(
        db_column='item_name'
    )
    material_id = models.CharField(
        db_column='material_id'
    )
    quantity_required = models.DecimalField(
        db_column='quantity_required',
        max_digits=10,
        decimal_places=2
    )
    unit_of_measure = models.CharField(
        db_column='unit_of_measure'
    )
    class Meta:
        managed = False
        db_table = 'product_rawmaterial'


class SelectProduct(models.Model):
    item_id = models.CharField(
        db_column='item_id',
        primary_key=True,
        max_length=255
    )
    item_name = models.CharField(
        db_column='item_name'
    )
    item_description = models.TextField(
        db_column='item_description'
    )

    class Meta:
        managed = False
        db_table = 'select_product'


class SelectMaterial(models.Model):
    item_id = models.CharField(
        db_column='item_id',
        primary_key=True,
        max_length=255
    )
    item_name = models.CharField(
        db_column='item_name'
    )
    unit_of_measure = models.CharField(
        db_column='unit_of_measure'
    )
    item_price = models.DecimalField(
        db_column='item_price',
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        managed = False
        db_table = 'select_material'