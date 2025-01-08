from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('blog/', task_list, name='task-list'),
    path('', register_page, name='register-page'),
    path('api/register/', RegisterAPI.as_view(), name='register-api'),
    path('api/login/', LoginAPI.as_view(), name='login-api'),
    path('api/blog/',BlogCreateView.as_view()),
    path('add_blog/',add_task),
    path('login/', login_view, name='login-page'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
