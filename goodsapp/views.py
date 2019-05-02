from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from menuapp.models import Menu
from .form import BookForm
from django.urls import reverse_lazy
# Create your views here.


class MenuList(ListView):
    queryset = Menu.objects.filter(parent_menu__isnull=True)


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('book_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('book_detail', kwargs={'pk': self.object.pk})
        return url


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('book_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('book_detail', kwargs={'pk': self.object.pk})
        return url


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
