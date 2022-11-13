from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from devices.models import (
    Device, TaskStatus, DeviceTask
)
from rest_framework.decorators import action
from rest_framework.response import Response
from devices.api.device.serializers import (
    DeviceSerializer, TaskStatusSerializer, DeviceTaskSerializer
)


class DeviceViewSet(ModelViewSet):

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    @action(detail=True, methods=['get'])
    def task(self, request, pk=None):
        device = self.get_object()
        if not device:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task = device.tasks.filter(status__name="START").first()
        if not task:
            return Response(
                {"status": {"name": False}}
            )
        task_serializer = DeviceTaskSerializer(instance=task)
        return Response(task_serializer.data)


class TaskStatusViewSet(ModelViewSet):

    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer


class DeviceTaskViewSet(ModelViewSet):

    queryset = DeviceTask.objects.all()
    serializer_class = DeviceTaskSerializer

    @action(detail=True, methods=['patch'])
    def change_status(self, request, pk=None):
        task = self.get_object()
        if not task:
            return Response(status=status.HTTP_404_NOT_FOUND)
        status_task = TaskStatus.objects.filter(
            name=request.data["name"])
        if not status_task:
            return Response({"status": {"name": False}})
        task.status = status_task.first()
        task.save()
        task_serializer = DeviceTaskSerializer(instance=task)
        return Response(task_serializer.data)
