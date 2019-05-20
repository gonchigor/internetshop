from orderapp.views import order_status_new
from .models import Cart, BookInCart
from goodsapp.models import Book
from django.views.generic.edit import UpdateView, DeleteView, FormMixin
from django.views.generic.detail import DetailView
from orderapp.form import OrderConfirmForm


# Create your views here.


class AddBookToCartView(UpdateView):
    model = BookInCart
    fields = ['quantity']
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
        context['url'] = self.request.META['HTTP_REFERER']
        return context

    def get_success_url(self):
        return self.request.POST['url']


class BookInCartDeleteView(DeleteView):
    model = BookInCart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = self.request.META['HTTP_REFERER']
        return context

    def get_success_url(self):
        return self.request.POST['url']


# class CartDetailView(DetailView, FormMixin):
class CartDetailView(DetailView):
    model = Cart
    # form_class = OrderConfirmForm

    def get_object(self, queryset=None):
        cart_id = self.request.GET.get('cart')
        cart = Cart.objects.get(pk=cart_id)
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get'] = self.request.GET
        return context

    # def get_initial(self):
    #     cart_id = self.request.session.get('cart-id', 0)
    #     initial = {
    #         'status': order_status_new,
    #         'cart': cart_id
    #     }
    #     return initial
