from django.db import models

# Create your models here.


class CurRates(models.Model):
    day = models.DateField("Дата", unique=True)
    rate = models.DecimalField("Курс доллара", max_digits=10, decimal_places=4)

    def __str__(self):
        return str(self.day)

    class Meta:
        verbose_name = "Курсы доллара"
        verbose_name_plural = "Курсы доллара"
