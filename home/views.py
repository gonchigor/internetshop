# from django.shortcuts import render
from goodsapp.models import Book
from goodsapp.views import BookListView
from django.views.generic.detail import DetailView
from cartapp.models import Cart, BookInCart


COUNT_CARDS = 6
# Create your views here.


class BookTopNewListView(BookListView):
    """Main page"""
    # queryset = Book.objects.order_by('-date_create')[:COUNT_CARDS]
    template_name = "home/index.html"

    def get_queryset(self):
        if 'search' in self.request.GET.keys() and self.request.GET['search']:
            return super().get_queryset()
        return Book.objects.order_by('-date_create')[:COUNT_CARDS]


class BookSearchListView(BookListView):
    """Search page"""
    # queryset = Book.objects.order_by('-date_create')[:COUNT_CARDS]
    template_name = "home/search.html"


class BookCustomerDetailView(DetailView):
    """Book for customers"""
    model = Book
    template_name = 'home/book_full.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart-id')
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
            book_in_cart_qs = BookInCart.objects.filter(cart=cart, book=self.object)
            if book_in_cart_qs.exists():
                context['cart_quantity'] = book_in_cart_qs.get().quantity
        return context
