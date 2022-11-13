from django.urls import path
from django.shortcuts import redirect
from django.contrib.admin.utils import unquote
from django.contrib import admin
from devices.models import DeviceTask, Device, TaskStatus
from devices.admin import ItemInTaskInLine, DeviceItemInLine

@admin.register(DeviceTask)
class DeviceTaskAdmin(admin.ModelAdmin):
    inlines = [
        ItemInTaskInLine
    ]
    readonly_fields = [
        "created",
    ]

@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    inlines = [
        DeviceItemInLine
    ]
    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.model_name
        urls = super().get_urls()
        my_urls = [
            path(
                '<path:object_id>/create_task/',
                self.create_task,
                name='%s_%s_create_task' % info
            ),
        ]
        return my_urls + urls

    def create_task(self, request, object_id):
        model = self.model
        obj = self.get_object(request, unquote(object_id))
        if obj is None:
            return self._get_obj_does_not_exist_redirect(request, model._meta, object_id)
        task = obj.make_task()
        url = "/admin/{0}/{1}/{2}/change/".format(
            self.model._meta.app_label,
            obj._meta.model_name,
            obj.pk
        )
        return redirect(url)
