from rest_framework import serializers
from .models import BOM

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOM
        fields = '__all__'