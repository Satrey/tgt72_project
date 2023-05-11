from django.contrib import admin
from .models import Device, DeviceType, DeviceModel, MobileProfile


class DeviceModelInline(admin.TabularInline):
    model = DeviceModel
    prepopulated_fields = {'slug': ('manufacturer', 'model',)}
    extra = 0


class MobileProfileAdmin(admin.ModelAdmin):
    model = MobileProfile


class DeviceAdmin(admin.ModelAdmin):
    model = Device
    list_display = ('address', 'model', 'device_type')
    list_filter = ('device_type', 'model', 'address')
    search_fields = ('address__address',)
    # fieldsets = (
    #     ('Main', {'fields': ('address', 'device_type', 'model')}),
    #     ('Departament', {'fields': (('serial_number', 'inventary_number',))}),
    #     ('Contact info', {'fields': ('phone_number_work', 'phone_number_mobile')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )


class DeviceModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('model',)}
    model = DeviceModel
    list_display = ('manufacturer', 'model', 'type',)
    list_filter = ('manufacturer', 'type', 'model')
    search_fields = ('manufacturer',)
    ordering = ('manufacturer', 'type', 'model',)


class DeviceTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('type',)}
    model = DeviceType
    inlines = (DeviceModelInline,)

    search_fields = ('type',)


admin.site.register(Device, DeviceAdmin)
admin.site.register(MobileProfile, MobileProfileAdmin)
admin.site.register(DeviceType, DeviceTypeAdmin)
admin.site.register(DeviceModel, DeviceModelAdmin)
