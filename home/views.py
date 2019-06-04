# from django.shortcuts import render
from goodsapp.models import Book, BookAction
from goodsapp.views import BaseBookListView
from django.views.generic.detail import DetailView
from cartapp.models import Cart, BookInCart
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from dimensionsapp.models import OrderStatus
from django.db.models import Count, Subquery, OuterRef

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
        context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2').\
            json()['Cur_OfficialRate']
        book_popular_id = BookInCart.objects.filter(cart__order__status=order_status_ok).values(
            'book').annotate(count=Count('cart')).filter(book=OuterRef('pk'))
        context['book_popular_list'] = Book.objects.annotate(count=Subquery(book_popular_id.values('count'))).order_by(
            '-count')[:COUNT_CARDS]
        book_action = BookAction.objects.filter(book=OuterRef('pk'))
        context['book_action_list'] = Book.objects.annotate(date_action=Subquery(
            book_action.values('date_update'))).order_by('-date_action')[:COUNT_CARDS]
        return context


class BookSearchListView(BaseBookListView):
    """Search page"""
    # queryset = Book.objects.order_by('-date_create')[:COUNT_CARDS]
    template_name = "home/search.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2').\
            json()['Cur_OfficialRate']
        return context


class CustomerBookDetailView(DetailView):
    """Book for customers"""
    model = Book
    template_name = 'home/book_full.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
            json()['Cur_OfficialRate']
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
