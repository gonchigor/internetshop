from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .form import BookForm
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.


class BookListView(ListView):
    model = Book

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
