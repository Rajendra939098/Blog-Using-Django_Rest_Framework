from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Task
from .serializer import TaskSerializer, LoginSerializer, RegisterSerializer


class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': "Successfully Registered"}, status=status.HTTP_201_CREATED)
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'status': True, 'message': 'User Login', 'Token': str(token)}, status=status.HTTP_200_OK)
            return Response({'status': False, 'message': "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProtectedEndpoint(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected endpoint"})


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        return Response({'message': 'Success'})
    return Response(serializer.errors)


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def register_page(request):
    return render(request, 'tasks/register.html')


def login_view(request):
    return render(request, 'tasks/login.html')
