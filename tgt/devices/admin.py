from django.contrib import admin
from .models import Device, DeviceType, DeviceModel


class DeviceModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('model',)}
    model = DeviceModel


class DeviceTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('type',)}
    model = DeviceType


admin.site.register(Device)
admin.site.register(DeviceType, DeviceTypeAdmin)
admin.site.register(DeviceModel, DeviceModelAdmin)
