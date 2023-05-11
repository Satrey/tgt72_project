from django.db import models
# from cross.models import CrossRoad


class Device(models.Model):
    address = models.ForeignKey('cross.CrossRoad', on_delete=models.CASCADE, verbose_name='Адрес установки')
    device_type = models.ForeignKey('DeviceType', on_delete=models.CASCADE, verbose_name='Тип устройства')
    model = models.ForeignKey('DeviceModel', on_delete=models.CASCADE, verbose_name='Модель устройства')
    serial_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Серийный номер')
    inventary_number = models.IntegerField(blank=True, null=True, verbose_name='Инвентарный номер')
    ip_address = models.GenericIPAddressField(default='192.168.70.1', verbose_name='IP Адрес устройства')
    mask = models.GenericIPAddressField(default='255.255.255.0', blank=True, null=True, verbose_name='Маска подсети')
    gateway = models.GenericIPAddressField(default='192.168.70.1', blank=True, null=True, verbose_name='Шлюз')
    mobile_profile = models.ForeignKey('MobileProfile', on_delete=models.PROTECT,
                                       blank=True, null=True, verbose_name='SIM Карта')

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"

    def __str__(self):
        return str(self.address)


class DeviceType(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True, verbose_name='Тип устройства')
    slug = models.SlugField(max_length=60, blank=True, null=True)

    class Meta:
        verbose_name = "Тип устройства"
        verbose_name_plural = "Типы устройств"

    def __str__(self):
        return str(self.type)


class DeviceModel(models.Model):
    manufacturer = models.CharField(max_length=50, blank=True, null=True, verbose_name='Проиводитель')
    model = models.CharField(max_length=100, blank=True, null=True, verbose_name='Модель оборудования')
    type = models.ForeignKey(DeviceType, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Тип устройства')
    slug = models.SlugField(max_length=120, blank=True, null=True, verbose_name='Слаг')

    class Meta:
        verbose_name = "Модель оборудования"
        verbose_name_plural = "Модели оборудования"

    def __str__(self):
        return str(self.model)


class MobileProfile(models.Model):
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    sim_number = models.CharField(max_length=25, verbose_name='Номер SIM карты')
    pin1 = models.CharField(max_length=6, blank=True, verbose_name='PIN код 1')
    pin2 = models.CharField(max_length=6, blank=True, verbose_name='PIN код 2')
    puk1 = models.CharField(max_length=12, blank=True, verbose_name='PUK код 1')
    puk2 = models.CharField(max_length=12, blank=True, verbose_name='PUK код 2')
    serial_number = models.CharField(max_length=20, blank=True, verbose_name='Серийный номер')
    dedicated_IP = models.GenericIPAddressField(blank=True, null=True, verbose_name='Выделенный IP адрес')
    open_vpn_IP = models.GenericIPAddressField(blank=True, null=True, verbose_name='Open VPN IP адрес')

    class Meta:
        verbose_name = 'SIM карта'
        verbose_name_plural = 'SIM карты'

    def __str__(self):
        return self.phone_number


