from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ProductMaterialViewSet, ProductRawMateialViewSet, SelectProductViewSet, SelectMaterialViewSet, insert_productmats

router = DefaultRouter()

router.register('productmaterial', ProductMaterialViewSet, basename='product-material')
router.register('productrawmaterial', ProductRawMateialViewSet, basename='product-raw')
router.register('selectproduct', SelectProductViewSet, basename='select-product')
router.register('selectmaterial', SelectMaterialViewSet, basename='select-material')

urlpatterns = [
    path('product_material/', include(router.urls)),
    path('insert_productmats/', insert_productmats, name='insert-productmats')
]