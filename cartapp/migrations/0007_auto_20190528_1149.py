# Generated by Django 2.2.1 on 2019-05-28 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0006_auto_20190517_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', related_query_name='cart', to=settings.AUTH_USER_MODEL),
        ),
    ]
