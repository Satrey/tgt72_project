from django.db import models


class CrossRoad(models.Model):
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = 'Перекрёсток'
        verbose_name_plural = 'Перекрёстки'

    def __str__(self):
        return self.address



