from django.contrib import admin
from .models import CrossRoad
from devices.models import Device


class DeviceInline(admin.TabularInline):
    model = Device
    extra = 0


class CrossRoadAdmin(admin.ModelAdmin):
    list_display = ('address', 'latitude', 'longitude',)
    ordering = ('address',)
    search_fields = ('address',)
    inlines = [DeviceInline]

    class Meta:
        model = CrossRoad

    fieldsets = (
        ('Местоположение', {'fields': ('address', 'latitude', 'longitude')}),
    )


admin.site.register(CrossRoad, CrossRoadAdmin)
