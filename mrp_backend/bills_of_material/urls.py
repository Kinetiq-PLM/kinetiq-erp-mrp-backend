from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import BOMViewSet

router = DefaultRouter()

router.register(r'bom', BOMViewSet)

urlpatterns = [
    path('bills_of_material/', include(router.urls)),
]