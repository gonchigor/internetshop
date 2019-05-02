from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField("Пункт меню", max_length=30, unique=True)
    url_name = models.CharField("Название ссылки", max_length=100)
    parent_menu = models.ForeignKey('Menu', on_delete=models.PROTECT, related_name='parent_menu_item',
                                    related_query_name='parent_menu_item', null=True, blank=True)

    def __str__(self):
        return self.name