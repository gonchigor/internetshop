from django.db import models
from django.contrib.auth import get_user_model
from goodsapp.models import Book
# Create your models here.

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', related_query_name='cart', blank=True,
                             null=True)
    date_create = models.DateTimeField("Дата создания", auto_now_add=True, )
    date_update = models.DateTimeField("Дата последнего изменения", auto_now=True)

    @property
    def total_quantity(self):
        quantity = self.books.aggregate(models.Sum('quantity'))['quantity__sum']
        if quantity is None:
            return 0
        return quantity

    @property
    def total_cost(self):
        return sum(book.cost for book in self.books.all())

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'


class BookInCart(models.Model):
    cart = models.ForeignKey(Cart, models.CASCADE, related_name='books', related_query_name='book')
    book = models.ForeignKey(Book, models.CASCADE, related_name='cart', related_query_name='cart')
    quantity = models.PositiveIntegerField('Количество', default=1)
    date_create = models.DateTimeField("Дата внесения", auto_now_add=True, )
    date_update = models.DateTimeField("Дата последнего изменения", auto_now=True)

    @property
    def cost(self):
        return self.quantity * self.book.price

    class Meta:
        verbose_name = 'книга в корзине'
        verbose_name_plural = 'книги в корзине'
        constraints = [
            models.UniqueConstraint(fields=['cart', 'book'], name='unique_book_in_cart'),
        ]

