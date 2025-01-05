from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'
        
class RegisterSerializer(serializers.ModelSerializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    confirm_password=serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self,data):
        if data['username']:
            if data['password'] != data.get('confirm_password'):
                raise serializers.ValidationError("Passwords do not match.")
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError("This Username Already Taken By Someone. Please Take Another User Name.")
            
            if data['email']:
                if User.objects.filter(email=data['email']).exists():
                    raise serializers.ValidationError("This Email is already registed in our Database. Use another Email id.")
        return data
    
    def create(self,validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        print(f"User {user.username} created successfully.")
        user.save()
        return user
