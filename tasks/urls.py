from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf import settings
from django.conf.urls.static import static


router=DefaultRouter()
router.register(r'tasks',TaskViewSet)

urlpatterns=[
    path('api/',include(router.urls)),
    path('',task_list)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)