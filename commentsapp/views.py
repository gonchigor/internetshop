from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment
from .form import CommentForm, CommentFormCreate
from orderapp.permissions import ManagerDeleteView, ManagerUpdateView
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
import requests
# Create your views here.


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentFormCreate
    
    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        initial['content_type'] = ContentType.objects.get(model=self.kwargs['model'])
        initial['object_id'] = self.kwargs['object_id']
        return initial

    def get_success_url(self):
        return self.request.POST.get('url', reverse_lazy('main-page'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usd_rate'] = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2').\
            json()['Cur_OfficialRate']
        return context


class CommentUpdateView(ManagerUpdateView):
    model = Comment
    form_class = CommentForm


class CommentDeleteView(ManagerDeleteView):
    model = Comment

    def get_success_url(self):
        pass
