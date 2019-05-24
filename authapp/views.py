from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from cartapp.models import Cart
from django.views.generic import TemplateView

# Create your views here.


class ShopLoginView(LoginView):
    template_name = 'authapp/login.html'

    def get_success_url(self):
        if self.request.user.has_perm('orderapp.manager'):
            return reverse_lazy('order_list')
        cart_id = self.request.session.get('cart-id')
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
            cart.user = self.request.user
            cart.save()
        return super().get_success_url()


class ShopPasswordChangeView(PasswordChangeView):
    template_name = 'authapp/password_change.html'
    success_url = reverse_lazy('auth:password_change_done')


class ShopPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'authapp/password_change_done.html'


class ShopLogoutView(LogoutView):
    next_page = reverse_lazy('main-page')


class ShopUserView(TemplateView):
    template_name = "authapp/user.html"
