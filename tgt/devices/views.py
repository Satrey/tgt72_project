from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Device


class DeviceListView(ListView):
    model = Device
    paginate_by = 12
