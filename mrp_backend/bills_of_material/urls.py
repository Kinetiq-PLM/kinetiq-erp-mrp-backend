from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import BillOfMaterialsViewSet

router = DefaultRouter()

router.register(r'billofmaterials', BillOfMaterialsViewSet)

urlpatterns = [
    path('bills_of_material/', include(router.urls)),
]