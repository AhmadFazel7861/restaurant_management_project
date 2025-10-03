from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone
from rest_framework.response import Response
from .models import Order, Coupon
from .serializers import OrderSerializer

class OrderHistoryAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class CouponValidationView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        code = request.data.get("code")

        if not code:
            return Response({"error": "Coupon code is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            coupon = Coupon.objects.get(
                code=code, 
                is_active=True,
                valid_until__gte=timezone.now().date()
                ) 
        except Coupon.DoesNotExist:
            return Response({"error": "Invalid or inactive coupon"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": "Coupon is valid.",
            "code": coupon.code,
            "discount_percentage": coupon.discount_percentage
        }, status=status.HTTP_200_OK)