from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import BillOfMaterials, NonProjectOrderPricing
from .serializers import BillOfMaterialsSerializer, NonProjectOrderPricingSerializer
from django.core.exceptions import ValidationError

class BillOfMaterialsViewSet(viewsets.ModelViewSet):
    queryset = BillOfMaterials.objects.all()
    serializer_class = BillOfMaterialsSerializer

class NonProjectOrderPricingViewSet(viewsets.ModelViewSet):
    queryset = NonProjectOrderPricing.objects.all()
    serializer_class = NonProjectOrderPricingSerializer