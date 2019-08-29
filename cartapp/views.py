from orderapp.views import order_status_new
from .models import Cart, BookInCart
from goodsapp.models import Book
from django.views.generic.edit import UpdateView, DeleteView, FormMixin
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from orderapp.permissions import ManagerUpdateView
import requests
from django.urls import reverse_lazy
from .form import AddBookToCartForm
from django.contrib.auth.views import redirect_to_login
from orderapp.form import OrderConfirmForm
from curratesapp.utils import RateContextMixin


# Create your views here.


class AddBookToCartView(RateContextMixin, UpdateView):
    model = BookInCart
    form_class = AddBookToCartForm
    template_name = 'cartapp/add_book_to_cart.html'

    def get_object(self, queryset=None):
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user
        cart_id = self.request.session.get('cart-id')
        cart, created_cart = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user})
        if created_cart:
            self.request.session['cart-id'] = cart.pk
        book = Book.objects.get(pk=self.kwargs['pk'])
        try:
            book_in_cart = BookInCart.objects.get(cart=cart, book=book)
        except BookInCart.DoesNotExist:
            book_in_cart = BookInCart(cart=cart, book=book)
        return book_in_cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            context['url'] = self.request.META['HTTP_REFERER']
        else:
            context['url'] = self.request.POST.get('url')
        # try:
        #     context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
        #         json()['Cur_OfficialRate']
        # except requests.ConnectionError:
        #     print('Can\'t get usd rate')
        return context

    def get_success_url(self):
        if 'add-and-cart' in self.request.POST.keys():
            return reverse_lazy('order_create')
        return self.request.POST['url']

    def get_initial(self):
        initial = super().get_initial()
        if self.request.method == 'GET':
            initial['url'] = self.request.META['HTTP_REFERER']
        return initial


class BookInCartDeleteView(RateContextMixin, DeleteView):
    model = BookInCart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = self.request.META['HTTP_REFERER']
        # try:
        #     context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
        #         json()['Cur_OfficialRate']
        # except requests.ConnectionError:
        #     print('Can\'t get usd rate')
        return context

    def get_success_url(self):
        return self.request.POST['url']


# class CartDetailView(DetailView, FormMixin):
class CartDetailView(RateContextMixin, DetailView):
    model = Cart
    # form_class = OrderConfirmForm

    def get_object(self, queryset=None):
        cart_id = self.request.GET.get('cart')
        cart = Cart.objects.get(pk=cart_id)
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get'] = self.request.GET
        # try:
        #     context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
        #         json()['Cur_OfficialRate']
        # except requests.ConnectionError:
        #     print('Can\'t get usd rate')
        return context

    # def get_initial(self):
    #     cart_id = self.request.session.get('cart-id', 0)
    #     initial = {
    #         'status': order_status_new,
    #         'cart': cart_id
    #     }
    #     return initial


class CartArchDetailView(LoginRequiredMixin, RateContextMixin, DetailView):
    model = Cart
    template_name = 'cartapp/cart_arhiv_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.order.last().user_comments.all().order_by('-date_create')
        # try:
        #     context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
        #         json()['Cur_OfficialRate']
        # except requests.ConnectionError:
        #     print('Can\'t get usd rate')
        return context


class CartCurrentDetailView(LoginRequiredMixin, RateContextMixin, DetailView):
    model = Cart
    template_name = 'cartapp/cart_current_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.order.last().user_comments.all().order_by('-date_create')
        # try:
        #     context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
        #         json()['Cur_OfficialRate']
        # except requests.ConnectionError:
        #     print('Can\'t get usd rate')
        return context


class BookInCartUpdateView(ManagerUpdateView):
    model = BookInCart
    fields = ['quantity']
    template_name = 'cartapp/add_book_to_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = self.request.META['HTTP_REFERER']
        return context

    def get_success_url(self):
        return self.request.POST['url']


