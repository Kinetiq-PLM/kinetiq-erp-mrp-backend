from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import BillOfMaterialsViewSet, NonProjectOrderPricingViewSet, ProductMatsViewSet, LaborCostViewSet, PrincipalItemsViewset, ProductRawMaterialCostViewSet, BOMListViewSet, OrderListViewSet, ProductPricingViewSet, CostOfRawMaterialsViewSet, OrderStatementViewSet, OrderProductionCostsViewSet, EmployeeOrderViewSet, insert_bom, NonProjectProductCostViewset, ProjectBOMDetailViewset, PrincipalItemOrderListViewset, insert_nonproject, PrincipalOrderItemViewSet, insert_principal, TrackingNpopViewSet, TrackingPrincipalViewSet

router = DefaultRouter()

router.register(r'billofmaterials', BillOfMaterialsViewSet)
router.register(r'nonprojectorderpricing', NonProjectOrderPricingViewSet)
router.register(r'productmats', ProductMatsViewSet)
router.register(r'laborcost', LaborCostViewSet)
router.register(r'principalitem', PrincipalItemsViewset)
router.register(r'product-costs', ProductRawMaterialCostViewSet, basename='product-costs')
router.register(r'bomlist', BOMListViewSet, basename='bom-list')
router.register(r'orderstatements', OrderStatementViewSet, basename='order-statement')
router.register(r'orderlist', OrderListViewSet, basename='order-list')
router.register(r'productpricing', ProductPricingViewSet, basename='product-pricing')
router.register(r'costofrawmats', CostOfRawMaterialsViewSet, basename='cost-raw')
router.register(r'orderproductioncost', OrderProductionCostsViewSet, basename='order-production')
router.register(r'employeeorder', EmployeeOrderViewSet, basename='employee-order')
router.register(r'npproductcost', NonProjectProductCostViewset, basename='np-productcost')
router.register(r'projectbomdetail', ProjectBOMDetailViewset, basename='project-bom')
router.register(r'principalorders', PrincipalItemOrderListViewset, basename='principal-orders')
router.register(r'principalitemorder', PrincipalOrderItemViewSet, basename='principal-items')
router.register(r'trackingnpop', TrackingNpopViewSet)
router.register(r'trackingprincipal', TrackingPrincipalViewSet)

urlpatterns = [
    path('bills_of_material/', include(router.urls)),
    path('insertbom/', insert_bom, name="insert-bom"),
    path('insert_nonproject/', insert_nonproject, name="insert-nonproject"),
    path('insert_principal/', insert_principal, name="insert-principal")
]