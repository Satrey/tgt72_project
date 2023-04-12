from django.contrib import admin
from .models import Device, DeviceType, DeviceModel


class DeviceAdmin(admin.ModelAdmin):
    model = Device

    list_display = ('address', 'model', 'device_type')
    search_fields = ('address', 'model__manufacturer',)
    list_filter = ('device_type', 'model', 'address')


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
