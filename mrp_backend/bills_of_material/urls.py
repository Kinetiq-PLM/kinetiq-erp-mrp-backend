from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import BillOfMaterialsViewSet, NonProjectOrderPricingViewSet, ProductMatsViewSet, LaborCostViewSet, ProductRawMaterialCostViewSet, BOMListViewSet, OrderListViewSet, ProductPricingViewSet, CostOfRawMaterialsViewSet, OrderStatementViewSet, OrderProductionCostsViewSet, EmployeeOrderViewSet

router = DefaultRouter()

router.register(r'billofmaterials', BillOfMaterialsViewSet)
router.register(r'nonprojectorderpricing', NonProjectOrderPricingViewSet)
router.register(r'productmats', ProductMatsViewSet)
router.register(r'laborcost', LaborCostViewSet)
router.register(r'product-costs', ProductRawMaterialCostViewSet, basename='product-costs')
router.register(r'bomlist', BOMListViewSet, basename='bom-list')
router.register(r'orderstatements', OrderStatementViewSet, basename='order-statement')
router.register(r'orderlist', OrderListViewSet, basename='order-list')
router.register(r'productpricing', ProductPricingViewSet, basename='product-pricing')
router.register(r'costofrawmats', CostOfRawMaterialsViewSet, basename='cost-raw')
router.register(r'orderproductioncost', OrderProductionCostsViewSet, basename='order-production')
router.register(r'employeeorder', EmployeeOrderViewSet, basename='employee-order')

urlpatterns = [
    path('bills_of_material/', include(router.urls)),
]