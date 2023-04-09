from django.contrib import admin
from .models import Device, DeviceType, DeviceModel


class DeviceAdmin(admin.ModelAdmin):
    model = Device

    search_fields = ('serial_number', 'inventory_number')
    list_filter = ('device_type', 'model')


class DeviceModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('model',)}
    model = DeviceModel
    list_filter = ('type', 'model')
    search_fields = ('manufacturer',)


class DeviceTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('type',)}
    model = DeviceType

    search_fields = ('type',)

admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceType, DeviceTypeAdmin)
admin.site.register(DeviceModel, DeviceModelAdmin)
