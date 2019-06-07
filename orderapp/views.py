from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from dimensionsapp.models import OrderStatus
from .models import Order
from .form import OrderConfirmForm, OrderCancelForm, OrderCustomerCommentForm, OrderFieldStatusForm, OrderForm
from cartapp.utils import CartContextMixin
from cartapp.models import Cart
from .permissions import ManagerListView, ManagerDetailView, ManagerUpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.contrib.auth.models import Group
from django.core.mail import send_mail

# python -m smtpd -n -c DebuggingServer localhost:1025
from django.contrib.auth.views import redirect_to_login

# Create your views here.
order_status_new = OrderStatus.objects.get_or_create(name='Новый')[0]
order_status_cancel_customer = OrderStatus.objects.get_or_create(name='Отменен покупателем')[0]
order_status_complect = OrderStatus.objects.get_or_create(name='Комплектуется')[0]


class OrderCreateView(CreateView, CartContextMixin):
    model = Order
    success_url = reverse_lazy('main-page')
    form_class = OrderConfirmForm
    # template_name = 'cartapp/cart_detail.html'

    def get_success_url(self):
        cart_id = self.request.session.pop('cart-id')
        g = Group.objects.get(name='Managers')
        mails = [u.email for u in g.user_set.all()]
        send_mail('Новый заказ', f'Поступил заказ №{cart_id} ', 'gg@myshop.sh', mails, fail_silently=True,)
        return reverse_lazy('cart_detail') + "?cart={}".format(cart_id)

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['cart'].initial = self.request.session.get('cart-id')
    #     form.fields['status'].initial = order_status_new.pk
    #     return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.cart = Cart.objects.get(pk=self.request.session.get('cart-id'))
        self.object.status = order_status_new
        self.object.save()
        for book_in_cart in self.object.cart.books.all():
            book = book_in_cart.book
            if book_in_cart.quantity < book.count_books:
                book.count_books -= book_in_cart.quantity
            else:
                book.count_books = 0
                book.is_active = False
            book.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
                json()['Cur_OfficialRate']
        except requests.ConnectionError:
            print('Can\'t get usd rate')
        return context

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial['name'] = self.request.user.first_name
            if self.request.user.email:
                initial['email'] = self.request.user.email
            initial['phone'] = self.request.user.extended.phone
            if self.request.user.extended.home_adress1:
                initial['delivery_adress'] = self.request.user.extended.home_adress1
            elif self.request.user.extended.home_adress2:
                initial['delivery_adress'] = self.request.user.extended.home_adress2
        initial['cart'] = self.request.session.get('cart-id')
        return initial


class ManagerOrderListView(ManagerListView):
    model = Order
    paginate_by = 15


class ManagerOrderDetailView(ManagerDetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.user_comments.all().order_by('-date_create')
        return context


class ManagerOrderActiveListView(ManagerOrderListView):
    template_name = 'orderapp/order_active_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(Q(status=order_status_new) | Q(status=order_status_complect)).\
            order_by('pk')


class ManagerOrderActiveDetailView(ManagerOrderDetailView):
    template_name = 'orderapp/order_active_detail.html'

    def get_queryset(self):
        return super().get_queryset().filter(Q(status=order_status_new) | Q(status=order_status_complect)).\
            order_by('pk')


class ManagerOrderUpdateView(ManagerUpdateView):
    model = Order
    template_name = 'orderapp/manager_order_form.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cart'] = self.object.cart
        return context


class ManagerOrderChangeStatusView(ManagerUpdateView):
    model = Order
    form_class = OrderFieldStatusForm
    template_name = 'orderapp/order_status_change.html'
    success_url = reverse_lazy('order_active_list')

    def get_queryset(self):
        return super().get_queryset().filter(Q(status=order_status_new) | Q(status=order_status_complect)).\
            order_by('pk')


class CustomerOrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderConfirmForm
    template_name = 'orderapp/customer_order_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.object.cart
        context['next'] = reverse_lazy('cart_detail_current', kwargs={'pk': self.object.cart.pk})
        context['is_new'] = self.object.status_id == order_status_new.pk
        try:
            context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
                json()['Cur_OfficialRate']
        except requests.ConnectionError:
            print('Can\'t get usd rate')
        return context

    def get_success_url(self):
        return reverse_lazy('cart_detail_current', kwargs={'pk': self.object.cart.pk})

    def get_queryset(self):
        return self.model._default_manager.filter(status=order_status_new, cart__user=self.request.user)


class CustomerOrderCancelView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderCancelForm
    template_name = 'orderapp/customer_order_cancel.html'
    initial = {'status': order_status_cancel_customer.pk}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.object.cart
        # context['next'] = reverse_lazy('cart_detail_current', kwargs={'pk': self.object.cart.pk})
        context['form'].fields['status'].instance = order_status_cancel_customer
        context['is_new'] = self.object.status_id == order_status_new.pk
        try:
            context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
                json()['Cur_OfficialRate']
        except requests.ConnectionError:
            print('Can\'t get usd rate')
        return context

    def get_success_url(self):
        return reverse_lazy('auth:user')+"?tab=3"

    def get_queryset(self):
        return self.model._default_manager.filter(status=order_status_new, cart__user=self.request.user)


class CustomerOrderCommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderCustomerCommentForm
    template_name = 'orderapp/customer_order_comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.object.cart
        context['is_new'] = self.object.status_id == order_status_new.pk
        # context['next'] = reverse_lazy('cart_detail_current', kwargs={'pk': self.object.cart.pk})
        try:
            context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
                json()['Cur_OfficialRate']
        except requests.ConnectionError:
            print('Can\'t get usd rate')
        return context

    def get_success_url(self):
        return reverse_lazy('auth:user')+"?tab=3"

    def get_queryset(self):
        return self.model._default_manager.filter(cart__user=self.request.user)
