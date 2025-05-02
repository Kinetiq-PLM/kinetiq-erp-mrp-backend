from rest_framework import serializers
from .models import ProductMaterial, ProductRawMaterial

class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterial
        fields = '__all__'

class ProductRawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRawMaterial
        fields = '__all__'