from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.permissions import IsAuthenticated


class MenuItemsListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
