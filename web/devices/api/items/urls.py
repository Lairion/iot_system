from django.urls import path, include
from rest_framework.routers import DefaultRouter
from devices.api.items.views import (
    ItemInTaskViewSet,
    ItemViewSet,
    DeviceItemViewSet
)

router = DefaultRouter()

router.register("items", ItemViewSet)
router.register("items_in_tasks", ItemInTaskViewSet)
router.register("device_items", DeviceItemViewSet)
