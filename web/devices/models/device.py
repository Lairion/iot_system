from django.db import models


class TaskStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def get_start():
    try:
        status = TaskStatus.objects.get(name="START")
    except:
        return None
    return status


class Device(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def make_task(self):
        task = DeviceTask.objects.create(device=self)
        for i in self.items.all():
            task.items_in_tasks.create(
                item=i.item,
                task=task,
                on=i.on,
                device_item=i
            )
        return task


class DeviceTask(models.Model):
    device = models.ForeignKey(
        "Device",
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    status = models.ForeignKey(
        "TaskStatus",
        null=True,
        blank=True,
        default=get_start,
        on_delete=models.SET_NULL
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device} {self.pk}"
