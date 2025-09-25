from django.shortcuts import render
from rest_framework.permisions import IsAuthenticated
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderHistoryAPI(APIView):
    permisions_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        serializer = OrderSerializer(oreders, many=True)
        return Response(serializer.data)

