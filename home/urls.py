from django.urls import path, include
from .views import BookTopNewListView, CustomerBookDetailView, BookSearchListView, MainRedirectView, \
    BookNavigationListView, CustomerJenreListView, CustomerJenreDetailView

urlpatterns = [
    path('', MainRedirectView.as_view(), name='start-page'),
    path('index/', BookTopNewListView.as_view(), name='main-page'),
    path('home/<int:pk>', CustomerBookDetailView.as_view(), name='book-detail-customer'),
    path('search/', BookSearchListView.as_view(), name='book-search'),
    path('catalog/', BookNavigationListView.as_view(), name='book-catalog'),
    path('jenre/', CustomerJenreListView.as_view(), name='book-jenre-list'),
    path('jenre/<int:pk>', CustomerJenreDetailView.as_view(), name='book-jenre-detail'),
]
