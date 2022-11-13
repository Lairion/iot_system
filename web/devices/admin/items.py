from django.contrib import admin
from devices.models import Item, ItemInTask, DeviceItem


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemInTask)
class ItemInTaskAdmin(admin.ModelAdmin):
    pass


@admin.register(DeviceItem)
class DeviceItemAdmin(admin.ModelAdmin):
    pass


class ItemInTaskInLine(admin.TabularInline):
    model = ItemInTask


class DeviceItemInLine(admin.TabularInline):
    model = DeviceItem
