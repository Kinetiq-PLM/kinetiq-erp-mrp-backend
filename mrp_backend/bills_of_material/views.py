from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import BOM
from .serializers import ItemSerializer
from django.core.exceptions import ValidationError

class BOMViewSet(viewsets.ModelViewSet):
    queryset = BOM.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs): #DRF and ModelViewSet calls this method automatically
        """Handles stock updates and applies business rules"""
        item = self.get_object()
        order_no = request.data.get("order_no", None)
        type = request.data.get("type", None)

        if order_no is None:
            return Response({"error": "Order no. is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if type is None:
            return Response({"error": "Type is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        item.saveOrder()
        # try:
        #     item.reduce_stock(int(order_qty))       #calls method from models.py
        #     return Response({"message": f"Stock updated! Remaining: {item.quantity}"})
        # except ValidationError as e:
        #     return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)