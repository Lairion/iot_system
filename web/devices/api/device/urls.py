from django.urls import path, include
from rest_framework.routers import DefaultRouter
from devices.api.device.views import (
    DeviceTaskViewSet,
    DeviceViewSet,
    TaskStatusViewSet
)

router = DefaultRouter()

router.register("devices", DeviceViewSet)
router.register("device_tasks", DeviceTaskViewSet)
router.register("task_statuses", TaskStatusViewSet)
