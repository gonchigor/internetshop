from django.urls import path
from .views import OrderCreateView, ManagerOrderListView, ManagerOrderDetailView, \
    CustomerOrderCancelView, CustomerOrderUpdateView, CustomerOrderCommentUpdateView, \
    ManagerOrderChangeStatusView, ManagerOrderUpdateView, ManagerOrderActiveListView, \
    ManagerOrderActiveDetailView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('all/', ManagerOrderListView.as_view(), name='order_list'),
    path('', ManagerOrderActiveListView.as_view(), name='order_active_list'),
    path('all/<int:pk>/', ManagerOrderDetailView.as_view(), name='order_detail'),
    path('<int:pk>/', ManagerOrderActiveDetailView.as_view(), name='order_active_detail'),
    path('<int:pk>/status/', ManagerOrderChangeStatusView.as_view(), name='order_change_status'),
    path('all/<int:pk>/update/', ManagerOrderUpdateView.as_view(), name='order_update'),
    path('cancel/<int:pk>/', CustomerOrderCancelView.as_view(), name='order_customer_cancel'),
    path('update/<int:pk>/', CustomerOrderUpdateView.as_view(), name='order_customer_update'),
    path('comment/<int:pk>/', CustomerOrderCommentUpdateView.as_view(), name='order_customer_comment'),
]
