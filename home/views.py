from django.shortcuts import render
from django.views.generic.list import ListView
from goodsapp.models import Book
from django.views.generic.detail import DetailView
from django.db.models import Q

COUNT_CARDS = 6
# Create your views here.


class BookTopNewListView(ListView):
    queryset = Book.objects.order_by('-date_create')[:COUNT_CARDS]
    template_name = "home/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'search' in self.request.GET.keys() and self.request.GET['search']:
            context['search_string'] = self.request.GET['search']
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'search' in self.request.GET.keys() and self.request.GET['search']:
            queryset = Book.objects.all()
            for s in self.request.GET['search'].split():
                queryset = queryset.filter(Q(authors__namePublic__icontains=s) | Q(name__icontains=s))
        return queryset


class BookCustomerDetailView(DetailView):
    model = Book
    template_name = 'home/book_full.html'
