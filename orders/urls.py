from django.urls import path
from .views import *

urlpatterns = [
    path('order-history/', OrderHistoryAPIView.as_view(), name='order-history'),
    
]