from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from menuapp.models import Menu


class MenuList(ListView):
    queryset = Menu.objects.filter(parent_menu__isnull=True)