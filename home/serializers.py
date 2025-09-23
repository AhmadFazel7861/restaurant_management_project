from res_framework import serializers
from .models import MenuCategory, MenuItem

class MenuCategorySerializer(serializers,ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']