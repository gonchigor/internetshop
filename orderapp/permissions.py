from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.views.generic import DeleteView


class ManagerAuthorizationRequired(PermissionRequiredMixin):
    permission_required = 'orderapp.manager'


class ManagerDetailView(ManagerAuthorizationRequired, DetailView):
    pass


class ManagerListView(ManagerAuthorizationRequired, ListView):
    pass


class ManagerCreateView(ManagerAuthorizationRequired, CreateView):
    pass


class ManagerUpdateView(ManagerAuthorizationRequired, UpdateView):
    pass


class ManagerDeleteView(ManagerAuthorizationRequired, DeleteView):
    pass
