from django.urls import path, include
from .views import AddBookToCartView

urlpatterns = [
    path('add/<int:pk>', AddBookToCartView.as_view(), name='add_book_to_cart')
]
