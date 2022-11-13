from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from devices.api.items.serializers import (
    ItemInTaskSerializer,
    DeviceItemSerializer
)

from devices.models import Device, TaskStatus, DeviceTask


class DeviceSerializer(ModelSerializer):

    items = DeviceItemSerializer(many=True)

    class Meta:
        model = Device
        fields = "__all__"


class TaskStatusSerializer(ModelSerializer):

    class Meta:
        model = TaskStatus
        fields = "__all__"


class DeviceTaskSerializer(ModelSerializer):

    status = TaskStatusSerializer()
    items_in_tasks = ItemInTaskSerializer(many=True)

    class Meta:
        model = DeviceTask
        fields = "__all__"
