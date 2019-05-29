from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from dimensionsapp.models import OrderStatus
from .models import Order
from .form import OrderConfirmForm, OrderCancelForm, OrderCustomerCommentForm
from cartapp.utils import CartContextMixin
from cartapp.models import Cart
from .permissions import ManagerListView, ManagerDetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
order_status_new = OrderStatus.objects.get(pk=1)
order_status_cancel_customer = OrderStatus.objects.get_or_create(name='Отменен покупателем')[0]


class OrderCreateView(CreateView, CartContextMixin):
    model = Order
    success_url = reverse_lazy('main-page')
    form_class = OrderConfirmForm
    # template_name = 'cartapp/cart_detail.html'

    def get_success_url(self):
        cart_id = self.request.session.pop('cart-id')
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
        return HttpResponseRedirect(self.get_success_url())


class ManagerOrderListView(ManagerListView):
    model = Order


class ManagerOrderDetailView(ManagerDetailView):
    model = Order


class CustomerOrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderConfirmForm
    template_name = 'orderapp/customer_order_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.object.cart
        context['next'] = reverse_lazy('cart_detail_current', kwargs={'pk': self.object.cart.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('cart_detail_current', kwargs={'pk': self.object.cart.pk})


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
        return context

    def get_success_url(self):
        return reverse_lazy('auth:user')+"?tab=3"


class CustomerOrderCommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderCustomerCommentForm
    template_name = 'orderapp/customer_order_comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.object.cart
        # context['next'] = reverse_lazy('cart_detail_current', kwargs={'pk': self.object.cart.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('auth:user')+"?tab=3"
