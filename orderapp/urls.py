from django.urls import path
from .views import OrderCreateView, ManagerOrderListView, ManagerOrderDetailView, \
    CustomerOrderCancelView, CustomerOrderUpdateView, CustomerOrderCommentUpdateView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('', ManagerOrderListView.as_view(), name='order_list'),
    path('<int:pk>/', ManagerOrderDetailView.as_view(), name='order_detail'),
    path('cancel/<int:pk>/', CustomerOrderCancelView.as_view(), name='order_customer_cancel'),
    path('update/<int:pk>/', CustomerOrderUpdateView.as_view(), name='order_customer_update'),
    path('comment/<int:pk>/', CustomerOrderCommentUpdateView.as_view(), name='order_customer_comment'),
]
