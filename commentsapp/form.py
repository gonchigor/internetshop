from django.forms import ModelForm, HiddenInput
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']


class CommentFormCreate(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', 'user', 'content_type', 'object_id']
        widgets = {
            'user': HiddenInput(),
            'content_type': HiddenInput(),
            'object_id': HiddenInput(),
        }
