from django.urls import path, include
from devices.api.device.urls import router as devices_router
from devices.api.items.urls import router as items_router


urlpatterns = [
    path("", include(devices_router.urls)),
    path("", include(items_router.urls)),
]
