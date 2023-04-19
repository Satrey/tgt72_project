from django.contrib import admin
from .models import CrossRoad
from devices.models import Device


class DeviceInline(admin.TabularInline):
    model = Device
    extra = 0


class CrossRoadAdmin(admin.ModelAdmin):
    model = CrossRoad
    list_display = ('address', 'number', 'latitude', 'longitude',)
    ordering = ('address',)
    search_fields = ('address',)
    inlines = [DeviceInline]

    fieldsets = (
        ('Местоположение', {'fields': ('address', 'number', 'latitude', 'longitude')}),
    )


admin.site.register(CrossRoad, CrossRoadAdmin)
