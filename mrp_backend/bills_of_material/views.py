from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import BillOfMaterials, NonProjectOrderPricing, ProductMats, LaborCost, PrincipalItems, ProductRawMaterialCost, BOMList, OrderList, ProductPricing, CostOfRawMaterials, OrderProductionCosts, EmployeeOrder, NonProjectProductCost, ProjectBOMDetail, NonProjectBOMDetail, PrincipalBOMDetail, PrincipalItemOrderList, PrincipalOrderItem, TrackingNpop, TrackingPrincipal, ProjectProductMats
from .serializers import BillOfMaterialsSerializer, NonProjectOrderPricingSerializer, ProductMatsSerializer, LaborCostSerializer, PrincipalItemsSerializer, ProductRawMaterialCostSerializer, BOMListSerializer, OrderListSerializer, ProductPricingSerializer, CostOfRawMaterialsSerializer, OrderStatementSerializer, OrderProductionCostSerializer, EmployeeOrderSerializer, NonProjectProductCostSerializer, ProjectBOMDetailSerializer, PrincipalItemOrderListSerializer, PrincipalOrderItemSerializer, TrackingNpopSerializer, TrackingPrincipalSerializer, ProjectProductMatsSerializer, NonProjectBOMDetailSerializer, PrincipalBOMDetailSerializer
from django.core.exceptions import ValidationError
from connected_modules.sales.models import Orders, StatementItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

class PrincipalItemsViewset(viewsets.ModelViewSet):
    queryset = PrincipalItems.objects.all()
    serializer_class = PrincipalItemsSerializer

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
    
class ProjectBOMDetailViewset(viewsets.ReadOnlyModelViewSet):
    queryset = ProjectBOMDetail.objects.all()
    serializer_class = ProjectBOMDetailSerializer

    @action(detail=False, methods=['get'], url_path='by-statement/(?P<statement_id>[^/.]+)')
    def get_products(self, request, statement_id=None):
        products_rm = ProjectBOMDetail.objects.filter(statement_id = statement_id)
        serializer_class = ProjectBOMDetailSerializer(products_rm,many=True)
        return Response(serializer_class.data)
    
class NonProjectBOMDetailViewset(viewsets.ReadOnlyModelViewSet):
    queryset = NonProjectBOMDetail.objects.all()
    serializer_class = NonProjectBOMDetailSerializer

    @action(detail=False, methods=['get'], url_path='by-statement/(?P<statement_id>[^/.]+)')
    def get_products(self, request, statement_id=None):
        products_rm = NonProjectBOMDetail.objects.filter(statement_id = statement_id)
        serializer_class = NonProjectBOMDetailSerializer(products_rm,many=True)
        return Response(serializer_class.data)
    
class PrincipalBOMDetailViewset(viewsets.ReadOnlyModelViewSet):
    queryset = PrincipalBOMDetail.objects.all()
    serializer_class = PrincipalBOMDetailSerializer

    @action(detail=False, methods=['get'], url_path='by-serviceid/(?P<service_order_item_id>[^/.]+)')
    def get_products(self, request, service_order_item_id=None):
        products_rm = PrincipalBOMDetail.objects.filter(service_order_item_id = service_order_item_id)
        serializer_class = PrincipalBOMDetailSerializer(products_rm,many=True)
        return Response(serializer_class.data)
    
class PrincipalItemOrderListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = PrincipalItemOrderList.objects.all()
    serializer_class = PrincipalItemOrderListSerializer

class PrincipalOrderItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PrincipalOrderItem.objects.all()
    serializer_class = PrincipalOrderItemSerializer

    @action(detail=False, methods=['get'], url_path='by-serviceid/(?P<service_order_id>[^/.]+)')
    def get_products(self, request, service_order_id=None):
        principal_product = PrincipalOrderItem.objects.filter(service_order_id = service_order_id)
        serializer_class = PrincipalOrderItemSerializer(principal_product,many=True)
        return Response(serializer_class.data)
    
class TrackingNpopViewSet(viewsets.ModelViewSet):
    queryset = TrackingNpop.objects.all()
    serializer_class = TrackingNpopSerializer

class TrackingPrincipalViewSet(viewsets.ModelViewSet):
    queryset = TrackingPrincipal.objects.all()
    serializer_class = TrackingPrincipalSerializer

class ProjectProductMatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProjectProductMats.objects.all()
    serializer_class = ProjectProductMatsSerializer

    @action(detail=False, methods=['get'], url_path='by-statement/(?P<statement_id>[^/.]+)')
    def get_productmats(self, request, statement_id=None):
        productmats = ProjectProductMats.objects.filter(statement_id = statement_id)
        serializer_class = ProjectProductMatsSerializer(productmats,many=True)
        return Response(serializer_class.data)

@api_view(['POST'])
def insert_bom(request):
    try:
        responses = []
        for entry in request.data:
            serializer = BillOfMaterialsSerializer(data=entry)
            if serializer.is_valid():
                serializer.save()
                responses.append({"data": serializer.data, "status": status.HTTP_201_CREATED})
            else:
                responses.append({"errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})
        
        return Response(responses, status=status.HTTP_207_MULTI_STATUS)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def insert_nonproject(request):
    try:
        if request.method == 'POST':
            serializer = NonProjectOrderPricingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def insert_principal(request):
    try:
        responses = []
        for entry in request.data:
            serializer = PrincipalItemsSerializer(data=entry)
            if serializer.is_valid():
                serializer.save()
                responses.append({"data": serializer.data, "status": status.HTTP_201_CREATED})
            else:
                responses.append({"errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})
        
        return Response(responses, status=status.HTTP_207_MULTI_STATUS)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@csrf_exempt
def update_tracking_status(request):
    if request.method == 'POST':
        try:
            import json
            data = json.loads(request.body)
            order_id = data.get('order_id')

            if not order_id:
                return JsonResponse({'error': 'Order ID is required'}, status=400)

            tracking_record = TrackingNpop.objects.filter(order_id=order_id).first()
            if tracking_record:
                tracking_record.status = 'Complete'
                tracking_record.save()
                return JsonResponse({'message': 'Status updated successfully'}, status=200)
            else:
                return JsonResponse({'error': 'Tracking record not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def update_tracking_status_principal(request):
    if request.method == 'POST':
        try:
            import json
            data = json.loads(request.body)
            service_order_item_id = data.get('service_order_item_id')

            if not service_order_item_id:
                return JsonResponse({'error': 'Service Order Id is required'}, status=400)

            tracking_record = TrackingPrincipal.objects.filter(service_order_item_id=service_order_item_id).first()
            if tracking_record:
                tracking_record.status = 'Complete'
                tracking_record.save()
                return JsonResponse({'message': 'Status updated successfully'}, status=200)
            else:
                return JsonResponse({'error': 'Tracking record not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)