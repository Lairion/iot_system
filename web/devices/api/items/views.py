from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from devices.models import (
    Item, ItemInTask, DeviceItem
)
from rest_framework.decorators import action
from rest_framework.response import Response
from devices.api.items.serializers import (
    ItemSerializer, ItemInTaskSerializer, DeviceItemSerializer
)


class ItemViewSet(ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemInTaskViewSet(ModelViewSet):

    queryset = ItemInTask.objects.all()
    serializer_class = ItemInTaskSerializer


class DeviceItemViewSet(ModelViewSet):

    queryset = DeviceItem.objects.all()
    serializer_class = DeviceItemSerializer
