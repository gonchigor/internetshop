from django.urls import path, include
from .views import BookTopNewListView, CustomerBookDetailView, BookSearchListView

urlpatterns = [
    path('', BookTopNewListView.as_view(), name='main-page'),
    path('home/<int:pk>', CustomerBookDetailView.as_view(), name='book-detail-customer'),
    path('search', BookSearchListView.as_view(), name='book-search'),
]
