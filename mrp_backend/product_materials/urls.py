from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ProductMaterialViewSet, ProductRawMateialViewSet

router = DefaultRouter()

router.register('productmaterial', ProductMaterialViewSet, basename='product-material')
router.register('productrawmaterial', ProductRawMateialViewSet, basename='product-raw')

urlpatterns = [
    path('product_material/', include(router.urls))
]