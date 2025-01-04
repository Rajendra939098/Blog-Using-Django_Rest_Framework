from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer


def task_list(request):
    tasks=Task.objects.all()
    return render(request,'tasks/task_list.html', {'tasks': tasks})
