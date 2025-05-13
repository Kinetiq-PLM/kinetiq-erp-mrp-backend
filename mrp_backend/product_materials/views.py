from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import ProductMaterial, ProductRawMaterial, SelectProduct, SelectMaterial
from .serializers import ProductMaterialSerializer, ProductRawMaterialSerializer, SelectProductSerializer, SelectMaterialSerializer
from bills_of_material.serializers import ProductMatsSerializer

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
    
class SelectProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SelectProduct.objects.all()
    serializer_class = SelectProductSerializer

class SelectMaterialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SelectMaterial.objects.all()
    serializer_class = SelectMaterialSerializer


@api_view(['POST'])
def insert_productmats(request):
    try:
        responses = []
        for entry in request.data:
            serializer = ProductMatsSerializer(data=entry)
            if serializer.is_valid():
                serializer.save()
                responses.append({"data": serializer.data, "status": status.HTTP_201_CREATED})
            else:
                responses.append({"errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})
        
        return Response(responses, status=status.HTTP_207_MULTI_STATUS)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)