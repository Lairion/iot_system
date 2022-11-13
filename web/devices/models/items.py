from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeviceItem(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    device = models.ForeignKey(
        "devices.Device",
        on_delete=models.CASCADE,
        related_name="items"
    )
    on = models.BooleanField(default=True)
    pins = models.CharField(max_length=20)

    def __str__(self):
        return str(self.item)


class ItemInTask(models.Model):
    item = models.ForeignKey(
        "Item",
        on_delete=models.CASCADE,
        related_name="items_in_tasks"
    )
    device_item = models.ForeignKey(
        "DeviceItem",
        on_delete=models.SET_NULL,
        null=True,
        related_name="items_in_tasks"
    )
    task = models.ForeignKey(
        "devices.DeviceTask",
        on_delete=models.CASCADE,
        related_name="items_in_tasks"
    )
    on = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.item} {self.pk}"
