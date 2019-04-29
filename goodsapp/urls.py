from django.urls import path
from goodsapp.views import BookDetailView, BookListView, BookCreateView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    ]
