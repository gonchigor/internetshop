from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from dimensionsapp.models import OrderStatus
from .models import Order
from .form import OrderConfirmForm
from cartapp.utils import CartContextMixin
from cartapp.models import Cart

# Create your views here.
order_status_new = OrderStatus.objects.get(pk=1)


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


