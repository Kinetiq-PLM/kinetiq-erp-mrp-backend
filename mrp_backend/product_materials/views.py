from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import ProductMaterial, ProductRawMaterial
from .serializers import ProductMaterialSerializer, ProductRawMaterialSerializer

class ProductMaterialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductMaterial.objects.all()
    serializer_class = ProductMaterialSerializer

class ProductRawMateialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductRawMaterial.objects.all()
    serializer_class = ProductRawMaterialSerializer

    @action(detail=False, methods=['get'], url_path='by-product/(?P<product_id>[^/.]+)')
    def get_rawmats(self, request, product_id=None):
        rawmats = ProductRawMaterial.objects.filter(product_id = product_id)
        serializer_class = ProductRawMaterialSerializer(rawmats,many=True)
        return Response(serializer_class.data)
