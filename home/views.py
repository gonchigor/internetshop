# from django.shortcuts import render
from goodsapp.models import Book, BookAction
from goodsapp.views import BaseBookListView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from cartapp.models import Cart, BookInCart
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from dimensionsapp.models import OrderStatus, Jenre
from django.db.models import Count, Subquery, OuterRef
from .form import JenreNavForm

import requests

order_status_ok = OrderStatus.objects.get_or_create(name='Доставлен')[0]
COUNT_CARDS = 6


# Create your views here.


class BookTopNewListView(BaseBookListView):
    """Main page"""
    # queryset = Book.objects.order_by('-date_create')[:COUNT_CARDS]
    template_name = "home/index.html"

    def get_queryset(self):
        if 'search' in self.request.GET.keys() and self.request.GET['search']:
            return super().get_queryset()
        return Book.objects.order_by('-date_create')[:COUNT_CARDS]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
        #     json()['Cur_OfficialRate']
        book_popular_id = BookInCart.objects.filter(cart__order__status=order_status_ok).values(
            'book').annotate(count=Count('cart')).filter(book=OuterRef('pk'))
        context['book_popular_list'] = Book.objects.annotate(count=Subquery(book_popular_id.values('count'))).order_by(
            '-count').filter(count__gt=0)[:COUNT_CARDS]
        context['book_action_list'] = Book.objects.filter(bookaction__pk__isnull=False).order_by(
            '-bookaction__date_update')[:COUNT_CARDS]
        return context


class BookSearchListView(BaseBookListView):
    """Search page"""
    # queryset = Book.objects.order_by('-date_create')[:COUNT_CARDS]
    template_name = "home/search.html"
    paginate_by = 10


class BookNavigationListView(BaseBookListView):
    template_name = "home/navigation.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
        #     json()['Cur_OfficialRate']
        initial = {}
        if 'j' in self.request.GET.keys():
            initial['j'] = self.request.GET.getlist('j')
        if 'p' in self.request.GET.keys():
            initial['p'] = self.request.GET.getlist('p')
        if 's' in self.request.GET.keys():
            initial['s'] = self.request.GET.getlist('s')
        if 'active' in self.request.GET.keys():
            initial['active'] = 'on'
        if 'search' in self.request.GET.keys() and self.request.GET['search']:
            initial['search'] = self.request.GET['search']
        context['nav_form'] = JenreNavForm(initial=initial)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'active' in self.request.GET.keys():
            queryset = queryset.filter(is_active=True)
        if 'j' in self.request.GET.keys():
            queryset = queryset.filter(jenre__pk__in=self.request.GET.getlist('j'))
        if 'p' in self.request.GET.keys():
            queryset = queryset.filter(publisher__pk__in=self.request.GET.getlist('p'))
        if 's' in self.request.GET.keys():
            queryset = queryset.filter(serie__pk__in=self.request.GET.getlist('s'))
        return queryset.distinct()


class CustomerBookDetailView(DetailView):
    """Book for customers"""
    model = Book
    template_name = 'home/book_full.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
                json()['Cur_OfficialRate']
        except requests.ConnectionError:
            print('Can\'t get usd rate')
        cart_id = self.request.session.get('cart-id')
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
            book_in_cart_qs = BookInCart.objects.filter(cart=cart, book=self.object)
            if book_in_cart_qs.exists():
                book_in_cart = book_in_cart_qs.get()
                context['cart_quantity'] = book_in_cart.quantity
                context['book_in_cart_id'] = book_in_cart.pk
        context['get_response'] = self.request.GET.urlencode()
        redirect = self.request.GET.get('type', 'main')
        if redirect == 'main':
            url_back = reverse_lazy('main-page')
        elif redirect == 'search':
            url_back = reverse_lazy('book-search') + '?search=' + self.request.GET.get('search', ' ')
        elif redirect == 'catalog':
            url_back = reverse_lazy('book-catalog')
        elif redirect == 'jenre':
            url_back = self.request.META['HTTP_REFERER']
        else:
            url_back = reverse_lazy('main-page')
        context['url'] = url_back
        if 'search' in self.request.GET.keys() and self.request.GET['search']:
            context['search_string'] = self.request.GET['search']
        context['comments'] = self.object.user_comments.all().order_by('-date_create')
        return context


class MainRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.has_perm('orderapp.manager'):
            return reverse_lazy('order_active_list')
        return reverse_lazy('main-page')


class CustomerJenreListView(ListView):
    queryset = Jenre.objects.filter(book__isnull=False).distinct()
    template_name = "home/jenre_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
                json()['Cur_OfficialRate']
        except requests.ConnectionError:
            print('Can\'t get usd rate')
        return context


class CustomerJenreDetailView(DetailView):
    queryset = Jenre.objects.filter(book__isnull=False).distinct()
    template_name = "home/jenre_books.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
                json()['Cur_OfficialRate']
        except requests.ConnectionError:
            print('Can\'t get usd rate')
        context['jenre_list'] = self.get_queryset()
        return context
