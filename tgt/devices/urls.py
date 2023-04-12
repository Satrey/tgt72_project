from django.urls import path
from .views import DeviceListView

urlpatterns = [
    path('device_list/', DeviceListView.as_view(), name='device_list')
]