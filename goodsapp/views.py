from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .form import BookForm
from dimensionsapp.models import Author
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.


class BookListView(ListView):
    model = Book

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'search' in self.request.GET.keys() and self.request.GET['search']:
            context['search_string'] = self.request.GET['search']
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'search' in self.request.GET.keys() and self.request.GET['search']:
            for s in self.request.GET['search'].split():
                authors = Author.objects.filter(namePublic__icontains=s).prefetch_related('book_set').values('book')
                # authors = Author.objects.filter(namePublic__icontains=s).values('book')
                queryset = queryset.filter(Q(name__icontains=s) | Q(pk__in=authors))
        return queryset


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
