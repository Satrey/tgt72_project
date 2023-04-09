from django.db import models
# from cross.models import CrossRoad


class Device(models.Model):
    address = models.ForeignKey('cross.CrossRoad', on_delete=models.CASCADE)
    device_type = models.ForeignKey('DeviceType', on_delete=models.CASCADE)
    model = models.ForeignKey('DeviceModel', on_delete=models.CASCADE)
    serial_number = models.IntegerField(verbose_name='Серийный номер')
    inventary_number = models.IntegerField(verbose_name='Инвентарный номер')
    ip_address = models.GenericIPAddressField(verbose_name='IP Адрес')

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"

    def __str__(self):
        return self.model.manufacturer + '  ' + self.model.model


class DeviceType(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True, verbose_name='Тип устройства')
    slug = models.SlugField(max_length=60, blank=True, null=True)

    class Meta:
        verbose_name = "Тип устройства"
        verbose_name_plural = "Типы устройств"

    def __str__(self):
        return self.type


class DeviceModel(models.Model):
    manufacturer = models.CharField(max_length=50, blank=True, null=True, verbose_name='Проиводитель')
    model = models.CharField(max_length=100, blank=True, null=True, verbose_name='Модель оборудования')
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Тип устройства')
    slug = models.SlugField(max_length=120, blank=True, null=True, verbose_name='Слаг')

    class Meta:
        verbose_name = "Модель оборудования"
        verbose_name_plural = "Модели оборудования"

    def __str__(self):
        return self.model
