from django.shortcuts import render
from .models import Cart, BookInCart
from goodsapp.models import Book
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

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

    def get_success_url(self):
        return reverse_lazy('book-detail-customer', args=[self.object.book.pk])
