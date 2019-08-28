# Generated by Django 2.2.4 on 2019-08-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurRates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='Дата')),
                ('rate', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Курс доллара')),
            ],
            options={
                'verbose_name': 'Курсы доллара',
                'verbose_name_plural': 'Курсы доллара',
            },
        ),
    ]
