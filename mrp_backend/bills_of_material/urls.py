from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import BillOfMaterialsViewSet, NonProjectOrderPricingViewSet, ProductMatsViewSet, LaborCostViewSet, ProductRawMaterialCostViewSet, BOMListViewSet

router = DefaultRouter()

router.register(r'billofmaterials', BillOfMaterialsViewSet)
router.register(r'nonprojectorderpricing', NonProjectOrderPricingViewSet)
router.register(r'productmats', ProductMatsViewSet)
router.register(r'laborcost', LaborCostViewSet)
router.register(r'product-costs', ProductRawMaterialCostViewSet, basename='product-costs')
router.register(r'bomlist', BOMListViewSet, basename='bom-list')

urlpatterns = [
    path('bills_of_material/', include(router.urls)),
]