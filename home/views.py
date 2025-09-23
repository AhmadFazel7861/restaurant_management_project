# from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import MenuCategory
from .models import MenuItem 
from .serializers import MenuCategorySerializer
from .serializers import MenuItemSerializer

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuItemPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param ='page_size'
    max_page_size = 100

class MenuItemViewSet(viewsets.ViewSet):
    pagination_class = MenuItemPagination

    def list(self, request):
        query = request.query_params.get('search',None)
        items = MenuItem.objects.all()

        if query:
            items = items.filter(name__icontains=query)

        paginator = self.pagination_class()
        paginated_items = paginator.paginate_queryset(items,request)

        serializer = MenuItemSerializer(paginated_items, many=True)
        return paginator.get_paginated_response(serializer.data)    