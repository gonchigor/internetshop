from django.urls import path, include
from .views import BookTopNewListView

urlpatterns = [
    path('', BookTopNewListView.as_view(), name='main-page'),
]
