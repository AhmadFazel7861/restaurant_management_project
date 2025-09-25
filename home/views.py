from rest_framework.generics import ListAPIView
from rest_framework import viewsets, status
from utils.validation_utils import is_valid_email
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import MenuCategory, MenuItem
from .serializers import MenuCategorySerializer, MenuItemSerializer
from django.shortcuts import get_object_or_404


class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuItemPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class MenuItemViewSet(viewsets.ViewSet):
    """
    ViewSet for listing menu items with optional search functionality.
    """
    pagination_class = MenuItemPagination

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return[IsAdminUser()]
        return [AllowAny()]    

    def list(self, request):
        search_query = request.query_params.get('search',None)
        category_query = request.query_params.get('category',None)
        
        items = MenuItem.objects.all()

        if search_query:
            items = items.filter(name__icontains=search_query)

        if category_query:
            items = items.filter(category__name__icontains=category_query)

        paginator = self.pagination_class()
        paginated_items = paginator.paginate_queryset(items,request)
        serializer = MenuItemSerializer(paginated_items, many=True)
        return paginator.get_paginated_response(serializer.data) 

    def update(self,request, pk=None):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        serializer = MenuItemSerializer(menu_item, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)     
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
