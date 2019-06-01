# from datetime import datetime
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from dimensionsapp.models import OrderStatus
from cartapp.models import Cart
from django.urls import reverse_lazy
from commentsapp.models import Comment

# Create your models here.


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, verbose_name='корзина', related_name='order',
                             related_query_name='order')
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, verbose_name='статус', related_name='order',
                               related_query_name='order')
    name = models.CharField(verbose_name='имя', max_length=50, help_text='Как к вам обращаться?')
    phone = models.CharField(max_length=15, verbose_name='телефон', help_text='Телефон для связи: +375(29)000-00-00')
    email = models.EmailField(verbose_name='email', blank=True, null=True,
                              help_text='Электронная почта: example@domain.com')
    delivery_adress = models.TextField(verbose_name='Адрес доставки',
                                       help_text='Пример: г. Минск, ул. Звездная, д. 1, кв. 7')
    comments = models.TextField(verbose_name='комментарий', blank=True, null=True)
    date_create = models.DateTimeField("Дата создания", auto_now_add=True, )
    date_update = models.DateTimeField("Дата последнего изменения", auto_now=True)
    user_comments = GenericRelation(Comment, related_query_name='order')

    def __str__(self):
        return "Заказ №" + str(self.pk) + " от " + self.date_create.strftime("%d.%m.%Y")

    @classmethod
    def get_list_url(cls):
        return reverse_lazy('order_list')

    @classmethod
    def get_active_list_url(cls):
        return reverse_lazy('order_active_list')

    def get_detail_url(self):
        return reverse_lazy('order_detail', kwargs={'pk': self.pk})

    def get_active_detail_url(self):
        return reverse_lazy('order_active_detail', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse_lazy('order_detail', kwargs={'pk': self.pk})

    def get_change_status_url(self):
        return reverse_lazy('order_change_status', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('order_update', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        permissions = [('manager', 'is_manager'), ]
