from django.contrib import admin
from .models import Device, DeviceType, DeviceModel

admin.site.register(Device)
admin.site.register(DeviceType)
admin.site.register(DeviceModel)
