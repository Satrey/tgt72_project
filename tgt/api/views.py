from turtle import position

from django.contrib.auth.models import Group
from cross.models import CrossRoad
from users.models import CustomUser, Position, Department
from tasks.models import Task
from devices.models import Device, DeviceModel, DeviceType

from rest_framework import viewsets, permissions
from .serializers import CustomUserSerializer, GroupSerializer, DeviceSerializer, PositionSerializer, \
    DepartmentSerializer, TaskSerializer


class PositionViewSet(viewsets.ModelViewSet):

    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartmentViewSet(viewsets.ModelViewSet):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CustomUserViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceViewSet(viewsets.ModelViewSet):

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

