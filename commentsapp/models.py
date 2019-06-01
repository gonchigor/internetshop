from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name='Пользователь')
    comment_text = models.TextField(verbose_name='Текст')
    date_create = models.DateTimeField(verbose_name='дата', auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
