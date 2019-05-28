from django.urls import path, include
from .views import AddBookToCartView, BookInCartDeleteView, CartDetailView, CartArchDetailView, CartCurrentDetailView

urlpatterns = [
    path('add/<int:pk>', AddBookToCartView.as_view(), name='add_book_to_cart'),
    path('delete/<int:pk>', BookInCartDeleteView.as_view(), name='book_in_cart_delete'),
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('cartarh/<int:pk>/', CartArchDetailView.as_view(), name='cart_detail_arch'),
    path('cartcur/<int:pk>/', CartCurrentDetailView.as_view(), name='cart_detail_current'),
]
