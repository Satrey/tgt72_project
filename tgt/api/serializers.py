from django.contrib.auth.models import Group
from django.template.defaultfilters import first

from cross.models import CrossRoad
from users.models import CustomUser, Department, Position
from tasks.models import Task
from devices.models import Device, DeviceModel, DeviceType

from rest_framework import serializers


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name', 'slug']


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department', 'slug']


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.StringRelatedField(many=False, read_only=True)
    position = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'middle_name', 'last_name', 'department', 'position']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    address = serializers.StringRelatedField(many=False, read_only=True)
    device_type = serializers.StringRelatedField(many=False, read_only=True)
    model = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Device
        fields = '__all__'


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    task_crossroad_address = serializers.StringRelatedField(many=False, read_only=True)
    task_receiver = serializers.StringRelatedField(many=False, read_only=True)
    task_worker = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
