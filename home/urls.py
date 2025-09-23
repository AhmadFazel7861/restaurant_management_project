from django.urls import path
from .views import *

menu_item_list = MenuItemViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('menu-categories/', MenuCategoryListView.as_view(), name='menu-categories'),
    path('menu-items/', menu_item_list(), name='menu-items-list'),
    
]