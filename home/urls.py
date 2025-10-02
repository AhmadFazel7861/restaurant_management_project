from django.urls import path
from .views import *

menu_item_list = MenuItemViewSet.as_view({'get': 'list'})
menu_item_update = MenuItemViewSet.as_view({'put': 'update', 'patch': 'partial_update'})

urlpatterns = [
    path('menu-categories/', MenuCategoryListView.as_view(), name='menu-categories'),
    path('menu-items/', menu_item_list, name='menu-items-list'),
    path('menu-items/<int:pk>/', menu_item_update, name='menu-items-update'),
    path('api/tables/<int:pk>/', TableDetailAPIView.as_view(), name='table-dtail'),
]