from django.urls import path
from .views import OrderCreateView, ManagerOrderListView, ManagerOrderDetailView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('', ManagerOrderListView.as_view(), name='order_list'),
    path('<int:pk>/', ManagerOrderDetailView.as_view(), name='order_detail'),
]
