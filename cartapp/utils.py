from .models import Cart
from django.views.generic.base import ContextMixin


class CartContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user
        cart_id = self.request.session.get('cart-id')
        cart, created_cart = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user})
        if created_cart:
            self.request.session['cart-id'] = cart.pk
        context['cart'] = cart
        return context
