from django.urls import path
from goodsapp.views import BookDetailView, BookListView, BookCreateView, BookUpdateView, BookDeleteView, \
    BookActionCreateView, BookActionDeleteView, BookActionDetailView, BookActionListView, BookActionUpdateView, \
    BookLoadView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('action/', BookActionListView.as_view(), name='book_action_list'),
    path('action/<int:pk>/', BookActionDetailView.as_view(), name='book_action_detail'),
    path('action/<int:pk>/update/', BookActionUpdateView.as_view(), name='book_action_update'),
    path('action/create/', BookActionCreateView.as_view(), name='book_action_create'),
    path('action/<int:pk>/delete/', BookActionDeleteView.as_view(), name='book_action_delete'),
    path('load/', BookLoadView.as_view(), name='book_load'),
]
