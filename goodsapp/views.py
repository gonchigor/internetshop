from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, BookAction
from .form import BookForm, BookActionForm, BookLoadForm
from dimensionsapp.models import Author
from django.urls import reverse_lazy
from django.db.models import Q
from orderapp.permissions import ManagerAuthorizationRequired, ManagerUpdateView, ManagerDeleteView, ManagerCreateView, \
    ManagerDetailView, ManagerListView
# import requests
from django.views.generic import FormView
from .csvload import loadcsv
# from django.http import HttpResponseRedirect
from curratesapp.utils import RateContextMixin


# Create your views here.


class BaseBookListView(RateContextMixin, ListView):
    """List with books.
        This is abstact model"""
    model = Book

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # try:
        #     context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
        #         json()['Cur_OfficialRate']
        # except requests.ConnectionError:
        #     print('Can\'t get usd rate')
        if 'search' in self.request.GET.keys() and self.request.GET['search']:
            context['search_string'] = self.request.GET['search']
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'search' in self.request.GET.keys() and self.request.GET['search']:
            for s in self.request.GET['search'].split():
                authors = Author.objects.filter(namePublic__icontains=s).values('book')
                queryset = queryset.filter(Q(name__icontains=s) | Q(pk__in=authors))
        return queryset


class BookListView(ManagerAuthorizationRequired, BaseBookListView):
    paginate_by = 15


class BookDetailView(ManagerDetailView):
    """Book view for managers """
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.user_comments.all().order_by('-date_create')
        return context


class BookCreateView(ManagerCreateView):
    model = Book
    form_class = BookForm

    # def get_success_url(self):
    #     url = super().get_success_url()
    #     if 'save-and-close' in self.request.POST.keys():
    #         url = reverse_lazy('book_list')
    #     elif 'save' in self.request.POST.keys():
    #         url = reverse_lazy('book_detail', kwargs={'pk': self.object.pk})
    #     return url


class BookUpdateView(ManagerUpdateView):
    model = Book
    form_class = BookForm

    # def get_success_url(self):
    #     url = super().get_success_url()
    #     if 'save-and-close' in self.request.POST.keys():
    #         url = reverse_lazy('book_list')
    #     elif 'save' in self.request.POST.keys():
    #         url = reverse_lazy('book_detail', kwargs={'pk': self.object.pk})
    #     return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookDeleteView(ManagerDeleteView):
    model = Book
    success_url = reverse_lazy('book_list')


class BookActionListView(ManagerListView):
    model = BookAction


class BookActionDetailView(ManagerDetailView):
    model = BookAction


class BookActionCreateView(ManagerCreateView):
    model = BookAction
    form_class = BookActionForm

    # def get_success_url(self):
    #     url = super().get_success_url()
    #     if 'save-and-close' in self.request.POST.keys():
    #         url = reverse_lazy('book_action_list')
    #     elif 'save' in self.request.POST.keys():
    #         url = reverse_lazy('book_action_detail', kwargs={'pk': self.object.pk})
    #     return url


class BookActionUpdateView(ManagerUpdateView):
    model = BookAction
    form_class = BookActionForm

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('book_action_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('book_action_detail', kwargs={'pk': self.object.pk})
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookActionDeleteView(ManagerDeleteView):
    model = BookAction
    success_url = reverse_lazy('book_action_list')


class BookLoadView(ManagerAuthorizationRequired, FormView):
    form_class = BookLoadForm
    template_name = "goodsapp/book_load.html"
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        loadcsv(self.request.FILES['file'])
        return super().form_valid(form)

