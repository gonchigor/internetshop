# from datetime import datetime

from django.db import models
from dimensionsapp.models import OrderStatus
from cartapp.models import Cart


# Create your models here.


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, verbose_name='корзина', related_name='order',
                             related_query_name='order')
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, verbose_name='статус', related_name='order',
                               related_query_name='order')
    name = models.CharField(verbose_name='имя', max_length=50)
    phone = models.CharField(max_length=15, verbose_name='телефон')
    email = models.EmailField(verbose_name='email', blank=True, null=True)
    delivery_adress = models.TextField(verbose_name='Адрес доставки')
    comments = models.TextField(verbose_name='комментарий', blank=True, null=True)
    date_create = models.DateTimeField("Дата создания", auto_now_add=True, )
    date_update = models.DateTimeField("Дата последнего изменения", auto_now=True)

    def __str__(self):
        return "Заказ №" + str(self.pk) + " от " + self.date_create.strftime("%d.%m.%Y")

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
