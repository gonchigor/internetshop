from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class UserExt(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    avatar = models.ImageField('аватар', blank=True, null=True, upload_to='avatars')
    phone = models.CharField('телефон', max_length=15)
    dop_info = models.TextField('дополнительная информация', blank=True, null=True)
    home_country = models.CharField('домашний адрес - страна', max_length=50, blank=True, null=True)
    home_city = models.CharField('домашний адрес - город', max_length=50, blank=True, null=True)
    home_index = models.CharField('домашний адрес - индекс', max_length=15, blank=True, null=True)
    home_adress1 = models.TextField('домашний адрес - адрес1', blank=True, null=True)
    home_adress2 = models.TextField('домашний адрес - адрес2', blank=True, null=True)

    class Meta:
        verbose_name = 'дополнительные параметры профиля'
        verbose_name_plural = 'дополнительные параметры профиля'

