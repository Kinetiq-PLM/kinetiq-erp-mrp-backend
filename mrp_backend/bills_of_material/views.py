from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import BillOfMaterials, NonProjectOrderPricing, ProductMats, LaborCost, ProductRawMaterialCost, BOMList
from .serializers import BillOfMaterialsSerializer, NonProjectOrderPricingSerializer, ProductMatsSerializer, LaborCostSerializer, ProductRawMaterialCostSerializer, BOMListSerializer
from django.core.exceptions import ValidationError

class BillOfMaterialsViewSet(viewsets.ModelViewSet):
    queryset = BillOfMaterials.objects.all()
    serializer_class = BillOfMaterialsSerializer

class NonProjectOrderPricingViewSet(viewsets.ModelViewSet):
    queryset = NonProjectOrderPricing.objects.all()
    serializer_class = NonProjectOrderPricingSerializer

class ProductMatsViewSet(viewsets.ModelViewSet):
    queryset = ProductMats.objects.all()
    serializer_class = ProductMatsSerializer

class LaborCostViewSet(viewsets.ModelViewSet):
    queryset = LaborCost.objects.all()
    serializer_class = LaborCostSerializer

class ProductRawMaterialCostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductRawMaterialCost.objects.all()
    serializer_class = ProductRawMaterialCostSerializer

class BOMListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BOMList.objects.all()
    serializer_class = BOMListSerializer