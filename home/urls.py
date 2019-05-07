from django.urls import path, include
from .views import BookTopNewListView, BookCustomerDetailView

urlpatterns = [
    path('', BookTopNewListView.as_view(), name='main-page'),
    path('<int:pk>', BookCustomerDetailView.as_view(), name='book-detail-customer'),
]
