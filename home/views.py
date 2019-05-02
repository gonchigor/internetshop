from django.shortcuts import render
from django.views.generic.list import ListView
from goodsapp.models import Book
from django.db.models import Q

COUNT_CARDS = 6
# Create your views here.


class BookTopNewListView(ListView):
    queryset = Book.objects.order_by('-date_create')[:COUNT_CARDS]
    template_name = "home/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'search' in self.request.GET.keys() and self.request.GET['search']:
            queryset = Book.objects.all()
            for s in self.request.GET['search'].split():
                # queryset = queryset.filter(name__iexact=s)
                queryset = queryset.filter(Q(authors__name__icontains=s) | Q(name__icontains=s))
            context['object_list'] = queryset
            context['search_string'] = self.request.GET['search']
        return context
