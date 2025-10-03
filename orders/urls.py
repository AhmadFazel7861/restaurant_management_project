from django.urls import path
from .views import *

urlpatterns = [
    path('order-history/', OrderHistoryAPIView.as_view(), name='order-history'),
    path("coupons/validate/", CouponValidationView.as_view(), name="coupon-validae"),
    
]