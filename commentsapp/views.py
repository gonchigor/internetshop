from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment
from .form import CommentForm
from orderapp.permissions import ManagerDeleteView, ManagerUpdateView

# Create your views here.


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm


class CommentUpdateView(ManagerUpdateView):
    model = Comment
    form_class = CommentForm


class CommentDeleteView(ManagerDeleteView):
    model = Comment

    def get_success_url(self):
        pass
