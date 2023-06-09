from django.db import models


class CrossRoad(models.Model):
    address = models.CharField(max_length=100, verbose_name="Адрес")
    number = models.IntegerField(null=True, blank=True, verbose_name='Номер перекрёстка')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Перекрёсток'
        verbose_name_plural = 'Перекрёстки'

    def __str__(self):
        return str(self.address)



