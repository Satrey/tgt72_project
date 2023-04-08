from django.contrib import admin
from .models import CrossRoad


class CrossRoadAdmin(admin.ModelAdmin):
    list_display = ('address', 'latitude', 'longitude',)
    ordering = ('address',)
    search_fields = ('address',)

    class Meta:
        model = CrossRoad


admin.site.register(CrossRoad, CrossRoadAdmin)
