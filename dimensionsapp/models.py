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

    def get_absolute_url(self):
        return reverse_lazy('author_detail', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


class Serie(Dimension):
    def get_absolute_url(self):
        return reverse_lazy('serie_detail', args=[self.pk, ])

    class Meta(Dimension.Meta):
        verbose_name = 'серия'
        verbose_name_plural = 'серии'


class Jenre(Dimension):
    def get_absolute_url(self):
        return reverse_lazy('jenre_detail', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class PublishingHouse(Dimension):
    def get_absolute_url(self):
        return reverse_lazy('publishing_house_detail', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = 'издательство'
        verbose_name_plural = 'издательства'


class FormatBook(Dimension):
    def get_absolute_url(self):
        return reverse_lazy('format_book_detail', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = 'формат'
        verbose_name_plural = 'форматы'


class Binding(Dimension):
    def get_absolute_url(self):
        return reverse_lazy('binding_detail', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = 'переплет'
        verbose_name_plural = 'переплеты'


class AgeRestriction(Dimension):
    def get_absolute_url(self):
        return reverse_lazy('age_restriction_detail', args=[self.pk])

    class Meta(Dimension.Meta):
        verbose_name = "возрастное ограничение"
        verbose_name_plural = "возрастные ограничения"
        ordering = ['description']


