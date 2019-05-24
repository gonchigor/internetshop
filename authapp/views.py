from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from cartapp.models import Cart

# Create your views here.


class ShopLoginView(LoginView):
    template_name = 'authapp/login.html'

    def get_success_url(self):
        cart_id = self.request.session.get('cart-id')
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
            cart.user = self.request.user
            cart.save()
        return super().get_success_url()


class ShopLogoutView(LogoutView):
    next_page = reverse_lazy('main-page')
