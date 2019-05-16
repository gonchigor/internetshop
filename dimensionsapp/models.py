from django.db import models
from django.urls import reverse_lazy

# Create your models here.


class Dimension(models.Model):
    name = models.CharField("Наименование", max_length=50, unique=True)
    description = models.TextField("Описание", blank=True, )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']


class Author(Dimension):
    biography = models.TextField("Биография", blank=True, )
    namePublic = models.CharField("Имя (для покупателя)", max_length=100)

    def get_absolute_url(self):
        return reverse_lazy('author_detail', args=[self.pk])

    @classmethod
    def get_list_url(cls):
        return reverse_lazy('author_list')

    @classmethod
    def get_create_url(cls):
        return reverse_lazy('author_create')

    def get_detail_url(self):
        return reverse_lazy('author_detail', args=[self.pk])

    def get_update_url(self):
        return reverse_lazy('author_update', args=[self.pk])

    def get_delete_url(self):
        return reverse_lazy('author_delete', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


class Serie(Dimension):
    def get_absolute_url(self):
        return reverse_lazy('serie_detail', args=[self.pk, ])

    @classmethod
    def get_list_url(cls):
        return reverse_lazy('serie_list')

    @classmethod
    def get_create_url(cls):
        return reverse_lazy('serie_create')

    def get_detail_url(self):
        return reverse_lazy('serie_detail', args=[self.pk])

    def get_update_url(self):
        return reverse_lazy('serie_update', args=[self.pk])

    def get_delete_url(self):
        return reverse_lazy('serie_delete', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = 'серия'
        verbose_name_plural = 'серии'


class Jenre(Dimension):
    def get_absolute_url(self):
        return reverse_lazy('jenre_detail', args=[self.pk])

    @classmethod
    def get_list_url(cls):
        return reverse_lazy('jenre_list')

    @classmethod
    def get_create_url(cls):
        return reverse_lazy('jenre_create')

    def get_detail_url(self):
        return reverse_lazy('jenre_detail', args=[self.pk])

    def get_update_url(self):
        return reverse_lazy('jenre_update', args=[self.pk])

    def get_delete_url(self):
        return reverse_lazy('jenre_delete', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class PublishingHouse(Dimension):
    def get_absolute_url(self):
        return reverse_lazy('publishing_house_detail', args=[self.pk])

    @classmethod
    def get_list_url(cls):
        return reverse_lazy('publishing_house_list')

    @classmethod
    def get_create_url(cls):
        return reverse_lazy('publishing_house_create')

    def get_detail_url(self):
        return reverse_lazy('publishing_house_detail', args=[self.pk])

    def get_update_url(self):
        return reverse_lazy('publishing_house_update', args=[self.pk])

    def get_delete_url(self):
        return reverse_lazy('publishing_house_delete', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = 'издательство'
        verbose_name_plural = 'издательства'


class FormatBook(Dimension):
    def get_absolute_url(self):
        return reverse_lazy('format_book_detail', args=[self.pk])

    @classmethod
    def get_list_url(cls):
        return reverse_lazy('format_book_list')

    @classmethod
    def get_create_url(cls):
        return reverse_lazy('format_book_create')

    def get_detail_url(self):
        return reverse_lazy('format_book_detail', args=[self.pk])

    def get_update_url(self):
        return reverse_lazy('format_book_update', args=[self.pk])

    def get_delete_url(self):
        return reverse_lazy('format_book_delete', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = 'формат'
        verbose_name_plural = 'форматы'


class Binding(Dimension):
    def get_absolute_url(self):
        return reverse_lazy('binding_detail', args=[self.pk])

    @classmethod
    def get_list_url(cls):
        return reverse_lazy('binding_list')

    @classmethod
    def get_create_url(cls):
        return reverse_lazy('binding_create')

    def get_detail_url(self):
        return reverse_lazy('binding_detail', args=[self.pk])

    def get_update_url(self):
        return reverse_lazy('binding_update', args=[self.pk])

    def get_delete_url(self):
        return reverse_lazy('binding_delete', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = 'переплет'
        verbose_name_plural = 'переплеты'


class AgeRestriction(Dimension):
    order = models.IntegerField('Номер в списке')

    def get_absolute_url(self):
        return reverse_lazy('age_restriction_detail', args=[self.pk])

    @classmethod
    def get_list_url(cls):
        return reverse_lazy('age_restriction_list')

    @classmethod
    def get_create_url(cls):
        return reverse_lazy('age_restriction_create')

    def get_detail_url(self):
        return reverse_lazy('age_restriction_detail', args=[self.pk])

    def get_update_url(self):
        return reverse_lazy('age_restriction_update', args=[self.pk])

    def get_delete_url(self):
        return reverse_lazy('age_restriction_delete', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = "возрастное ограничение"
        verbose_name_plural = "возрастные ограничения"
        ordering = ['order']


class OrderStatus(Dimension):
    def get_absolute_url(self):
        return reverse_lazy('order_status_detail', args=[self.pk])

    @classmethod
    def get_list_url(cls):
        return reverse_lazy('order_status_list')

    @classmethod
    def get_create_url(cls):
        return reverse_lazy('order_status_create')

    def get_detail_url(self):
        return reverse_lazy('order_status_detail', args=[self.pk])

    def get_update_url(self):
        return reverse_lazy('order_status_update', args=[self.pk])

    def get_delete_url(self):
        return reverse_lazy('order_status_delete', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = 'статус заказа'
        verbose_name_plural = 'статусы заказа'


