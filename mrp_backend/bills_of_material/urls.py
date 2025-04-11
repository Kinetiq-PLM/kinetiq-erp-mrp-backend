from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import BillOfMaterialsViewSet, NonProjectOrderPricingViewSet, ProductMatsViewSet, LaborCostViewSet

router = DefaultRouter()

router.register(r'billofmaterials', BillOfMaterialsViewSet)
router.register(r'nonprojectorderpricing', NonProjectOrderPricingViewSet)
router.register(r'productmats', ProductMatsViewSet)
router.register(r'laborcost', LaborCostViewSet)

urlpatterns = [
    path('bills_of_material/', include(router.urls)),
]