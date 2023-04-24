from django.urls import path, include
from rest_framework import routers
from .views import CustomUserViewSet, GroupViewSet, DeviceViewSet, PositionViewSet, DepartmentViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
]