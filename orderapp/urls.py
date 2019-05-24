from django.urls import path
from .views import OrderCreateView, ManagerOrderListView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('', ManagerOrderListView.as_view(), name='order_list')
]
