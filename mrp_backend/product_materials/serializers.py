from rest_framework import serializers
from .models import ProductMaterial, ProductRawMaterial, SelectProduct, SelectMaterial

class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterial
        fields = '__all__'

class ProductRawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRawMaterial
        fields = '__all__'

class SelectProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectProduct
        fields = '__all__'

class SelectMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectMaterial
        fields = '__all__'