from django.db import models
from dimensionsapp import models as referen
from django.urls import reverse_lazy
from django.contrib.contenttypes.fields import GenericRelation
from commentsapp.models import Comment
# Create your models here.


class Book(models.Model):
    name = models.CharField("Название книги", max_length=200)
    image_field = models.ImageField("Фото обложки", blank=True, null=True, upload_to='bookimage')
    price = models.DecimalField("Цена (BYN)", max_digits=8, decimal_places=2)
    authors = models.ManyToManyField(referen.Author, verbose_name="Авторы")
    serie = models.ForeignKey(referen.Serie, on_delete=models.PROTECT, verbose_name="Серия", null=True, blank=True)
    jenre = models.ManyToManyField(referen.Jenre, verbose_name="Жанры")
    year_publishing = models.PositiveIntegerField("Год издания")
    count_pages = models.PositiveIntegerField("Количество страниц")
    binding = models.ForeignKey(referen.Binding, on_delete=models.PROTECT, verbose_name="Переплет")
    format_book = models.ForeignKey(referen.FormatBook, on_delete=models.PROTECT, verbose_name="Формат")
    isbn = models.CharField("ISBN", max_length=13)
    weight = models.FloatField("Вес (гр)")
    age_restrictions = models.ForeignKey(referen.AgeRestriction, verbose_name="Возрастные ограничения",
                                         on_delete=models.PROTECT, )
    publisher = models.ForeignKey(referen.PublishingHouse, on_delete=models.PROTECT, verbose_name="Издательство")
    count_books = models.PositiveIntegerField("Количество книг в наличии")
    is_active = models.BooleanField("Активный (доступен для заказа)", default=True)
    rate = models.FloatField("Рейтинг")
    date_create = models.DateTimeField("Дата внесения в каталог", auto_now_add=True, )
    date_update = models.DateTimeField("Дата последнего изменения карточки", auto_now=True)
    user_comments = GenericRelation(Comment, related_query_name='book')

    def description(self):
        return ', '.join([s.namePublic for s in self.authors.all()]) + " \"" + self.name + "\""

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.pk})

    @classmethod
    def get_list_url(cls):
        return reverse_lazy('book_list')

    @classmethod
    def get_create_url(cls):
        return reverse_lazy('book_create')

    def get_detail_url(self):
        return reverse_lazy('book_detail', args=[self.pk])

    def get_update_url(self):
        return reverse_lazy('book_update', args=[self.pk])

    def get_delete_url(self):
        return reverse_lazy('book_delete', args=[self.pk])

    def get_detail_customer_url(self):
        return reverse_lazy('book-detail-customer', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"
