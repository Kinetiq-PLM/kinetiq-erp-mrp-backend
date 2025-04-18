from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import BillOfMaterials, NonProjectOrderPricing, ProductMats, LaborCost, ProductRawMaterialCost, BOMList, OrderList, ProductPricing, CostOfRawMaterials, OrderProductionCosts, EmployeeOrder, NonProjectProductCost
from .serializers import BillOfMaterialsSerializer, NonProjectOrderPricingSerializer, ProductMatsSerializer, LaborCostSerializer, ProductRawMaterialCostSerializer, BOMListSerializer, OrderListSerializer, ProductPricingSerializer, CostOfRawMaterialsSerializer, OrderStatementSerializer, OrderProductionCostSerializer, EmployeeOrderSerializer, NonProjectProductCostSerializer
from django.core.exceptions import ValidationError
from connected_modules.sales.models import Orders, StatementItem

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

class OrderListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer

class OrderStatementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderStatementSerializer

    @action(detail=False, methods=['get'], url_path='by-order/(?P<order_id>[^/.]+)')
    def get_statement(self, request, order_id=None):
        products = Orders.objects.filter(order_id = order_id)
        serializer_class = OrderStatementSerializer(products,many=True)
        return Response(serializer_class.data)

class ProductPricingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductPricing.objects.all()
    serializer_class = ProductPricingSerializer

    @action(detail=False, methods=['get'], url_path='by-statement/(?P<statement_id>[^/.]+)')
    def get_products(self, request, statement_id=None):
        products = ProductPricing.objects.filter(statement_id = statement_id)
        serializer_class = ProductPricingSerializer(products,many=True)
        return Response(serializer_class.data)

class CostOfRawMaterialsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CostOfRawMaterials.objects.all()
    serializer_class = CostOfRawMaterialsSerializer

    @action(detail=False, methods=['get'], url_path='by-product/(?P<product_id>[^/.]+)')
    def get_products(self, request, product_id=None):
        rawmats = CostOfRawMaterials.objects.filter(product_id = product_id)
        serializer_class = CostOfRawMaterialsSerializer(rawmats,many=True)
        return Response(serializer_class.data)
    
class OrderProductionCostsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderProductionCosts.objects.all()
    serializer_class = OrderProductionCostSerializer

    @action(detail=False, methods=['get'], url_path='(?P<order_id>[^/.]+)')
    def get_products(self, request, order_id=None):
        orders = OrderProductionCosts.objects.filter(order_id = order_id)
        serializer_class = OrderProductionCostSerializer(orders,many=True)
        return Response(serializer_class.data)
    
class EmployeeOrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeOrder.objects.all()
    serializer_class = EmployeeOrderSerializer

    @action(detail=False, methods=['get'], url_path='(?P<order_id>[^/.]+)')
    def get_products(self, request, order_id=None):
        ordersemployee = EmployeeOrder.objects.filter(order_id = order_id)
        serializer_class = EmployeeOrderSerializer(ordersemployee,many=True)
        return Response(serializer_class.data)
    
class NonProjectProductCostViewset(viewsets.ReadOnlyModelViewSet):
    queryset = NonProjectProductCost.objects.all()
    serializer_class = NonProjectProductCostSerializer
    
    @action(detail=False, methods=['get'], url_path='statement/(?P<statement_id>[^/.]+)')
    def get_npproducts(self, request, statement_id=None):
        npproducts = NonProjectProductCost.objects.filter(statement_id = statement_id)
        serializer_class = NonProjectProductCostSerializer(npproducts,many=True)
        return Response(serializer_class.data)

@api_view(['POST'])
def insert_bom(request):
    if request.method == 'POST':
        serializer = BillOfMaterialsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data saved successfully", "data": serializer.data}, status=201)
        return Response(serializer.errors, status=400)