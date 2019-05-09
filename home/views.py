# from django.shortcuts import render
from goodsapp.models import Book
from goodsapp.views import BookListView
from django.views.generic.detail import DetailView


COUNT_CARDS = 6
# Create your views here.


class BookTopNewListView(BookListView):
    # queryset = Book.objects.order_by('-date_create')[:COUNT_CARDS]
    template_name = "home/index.html"

    def get_queryset(self):
        if 'search' in self.request.GET.keys() and self.request.GET['search']:
            return super().get_queryset()
        return Book.objects.order_by('-date_create')[:COUNT_CARDS]


class BookCustomerDetailView(DetailView):
    model = Book
    template_name = 'home/book_full.html'
