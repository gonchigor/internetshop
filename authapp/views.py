from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from cartapp.models import Cart
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .forms import UserForm, UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth import login, get_user_model
from django.contrib.auth.models import Group
from .models import UserExt
from PIL import Image
# Create your views here.
Customers = Group.objects.get(name="Customers")
User = get_user_model()


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
        if user_ext.avatar:
            im = Image.open(user_ext.avatar.path)
            im = im.resize((191, 264))
            im.save(user_ext.avatar.path)
        login(self.request, self.object)
        return response


class SelfUserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "authapp/user.html"

    def get_object(self, queryset=None):
        return self.request.user


class SelfUserUpdateView(LoginRequiredMixin, UpdateView):
    model = UserExt
    form_class = UserUpdateForm
    success_url = reverse_lazy('auth:user')

    def get_object(self, queryset=None):
        return self.request.user.extended

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['email'].initial = self.request.user.email
        context['form'].fields['first_name'].initial = self.request.user.first_name
        context['form'].fields['last_name'].initial = self.request.user.last_name
        return context

    def form_valid(self, form):
        user = self.request.user
        user.email = form.cleaned_data['email']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        response = super().form_valid(form)
        if 'avatar' in form.changed_data and self.object.avatar:
            im = Image.open(self.object.avatar.path)
            im = im.resize((191, 264))
            im.save(self.object.avatar.path)
        return response
