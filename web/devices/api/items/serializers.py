from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from devices.models import Item, ItemInTask, DeviceItem


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"


class ItemInTaskSerializer(ModelSerializer):

    item = ItemSerializer()

    class Meta:
        model = ItemInTask
        fields = "__all__"


class DeviceItemSerializer(ModelSerializer):

    item = ItemSerializer()

    class Meta:
        model = DeviceItem
        fields = "__all__"
