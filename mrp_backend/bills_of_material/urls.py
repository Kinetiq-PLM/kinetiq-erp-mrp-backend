from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import BillOfMaterialsViewSet, NonProjectOrderPricingViewSet

router = DefaultRouter()

router.register(r'billofmaterials', BillOfMaterialsViewSet)
router.register(r'nonprojectorderpricing', NonProjectOrderPricingViewSet)

urlpatterns = [
    path('bills_of_material/', include(router.urls)),
]