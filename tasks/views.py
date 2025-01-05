from pyexpat.errors import messages
from django.shortcuts import redirect, render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .serializer import *
from rest_framework.authtoken.models import Token
# Create your views here.


class RegisterAPI(APIView):

    def post(self,request):
        data=request.data 
        serializer=RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors
            },status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'status':True,'message':"Successfully Registered"},status.HTTP_201_CREATED)

class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer


def task_list(request):
    tasks=Task.objects.all()
    return render(request,'tasks/task_list.html', {'tasks': tasks})

def register_page(request):
    return render(request, 'tasks/register.html')



