from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from cartapp.models import Cart
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .models import UserExt
# Create your views here.
Customers = Group.objects.get(name="Customers")


class ShopLoginView(LoginView):
    template_name = 'authapp/login.html'

    def get_success_url(self):
        if self.request.user.has_perm('orderapp.manager'):
            return reverse_lazy('order_list')
        cart_id = self.request.session.get('cart-id')
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
            cart.user = self.request.user
            cart.save()
        return super().get_success_url()


class ShopPasswordChangeView(PasswordChangeView):
    template_name = 'authapp/password_change.html'
    success_url = reverse_lazy('auth:password_change_done')


class ShopPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'authapp/password_change_done.html'


class ShopLogoutView(LogoutView):
    next_page = reverse_lazy('main-page')


class ShopUserView(TemplateView):
    template_name = "authapp/user.html"


class RegistrationUserView(CreateView):
    form_class = UserForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('main-page')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.email = form.cleaned_data['email']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.save()
        self.object.groups.add(Customers)
        user_ext = UserExt(
            user=self.object,
            phone=form.cleaned_data['phone'],
            home_country=form.cleaned_data['home_country'],
            home_city=form.cleaned_data['home_city'],
            home_index=form.cleaned_data['home_index'],
            home_adress1=form.cleaned_data['home_adress1'],
            home_adress2=form.cleaned_data['home_adress2'],
            dop_info=form.cleaned_data['dop_info'],
            avatar=form.cleaned_data['avatar']
        )
        user_ext.save()
        login(self.request, self.object)
        return response
