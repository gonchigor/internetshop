from django.urls import path, include
from .views import AddBookToCartView, BookInCartDeleteView

urlpatterns = [
    path('add/<int:pk>', AddBookToCartView.as_view(), name='add_book_to_cart'),
    path('delete/<int:pk>', BookInCartDeleteView.as_view(), name='book_in_cart_delete'),
    # path('', CartDetailView.as_view(), name='cart_detail')
]
