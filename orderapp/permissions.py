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
    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = self.object.get_list_url()
        elif 'save' in self.request.POST.keys():
            url = self.object.get_detail_url()
        return url


class ManagerUpdateView(ManagerAuthorizationRequired, UpdateView):
    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = self.object.get_list_url()
        elif 'save' in self.request.POST.keys():
            url = self.object.get_detail_url()
        return url


class ManagerDeleteView(ManagerAuthorizationRequired, DeleteView):
    pass
