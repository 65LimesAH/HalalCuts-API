from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'item',
            'slug',
            'description',
            'price',
            'scale',
            'created',
            'updated',
            'active',
            'primary_category',
        )
