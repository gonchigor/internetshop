from django.shortcuts import render
from django.views.generic.list import ListView
from goodsapp.models import Book

COUNT_CARDS = 5
# Create your views here.


class BookTopNewListView(ListView):
    queryset = Book.objects.order_by('-date_create')[COUNT_CARDS]
