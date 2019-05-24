from django.urls import path, include
from .views import ShopLoginView, ShopLogoutView

app_name = 'auth'
urlpatterns = [
    path('login/', ShopLoginView.as_view(), name='log_in'),
    path('logout', ShopLogoutView.as_view(), name='log_out')
]
