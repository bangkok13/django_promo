import datetime
from django.db import models
from django.utils import timezone


class Promo(models.Model):
    name = models.CharField('имя', max_length=80)
    promo = models.CharField('промо', max_length=80)
    date = models.DateTimeField('дата')

    class Meta:
        verbose_name = 'Промо'
        verbose_name_plural = 'Промо'

    def __str__(self):
        return  self.name