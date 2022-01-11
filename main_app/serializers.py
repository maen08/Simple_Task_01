from django.db import models
from .models import Task
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Task



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
        ]
    
        