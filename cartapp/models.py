from django.db import models
from django.contrib.auth import get_user_model
from goodsapp.models import Book
# Create your models here.

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', related_query_name='user', blank=True,
                             null=True)
    date_create = models.DateTimeField("Дата создания", auto_now_add=True, )
    date_update = models.DateTimeField("Дата последнего изменения", auto_now=True)

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'


class BookInCart(models.Model):
    cart = models.ForeignKey(Cart, models.CASCADE, related_name='cart', related_query_name='cart')
    book = models.ForeignKey(Book, models.CASCADE, related_name='book', related_query_name='book')
    quantity = models.PositiveIntegerField('Количество', default=1)
    date_create = models.DateTimeField("Дата внесения", auto_now_add=True, )
    date_update = models.DateTimeField("Дата последнего изменения", auto_now=True)

    class Meta:
        verbose_name = 'книга в корзине'
        verbose_name_plural = 'книги в корзине'
        constraints = [
            models.UniqueConstraint(fields=['cart', 'book'], name='unique_book_in_cart'),
        ]

