from http.client import ResponseNotReady
from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import TaskSerializer, UserSerializer
from rest_framework.response import Response
from .models import Task
from django.contrib.auth.models import User

class TaskView(viewsets.ViewSet):
    def create(self,request):
        """create new task"""
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    
    def list(self,request):
        """list all tasks encluding previous tasks"""
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class UserView(viewsets.ViewSet):
    """get list of all users - returns their emails"""
    def list(self,request):
        users = User.objects.all()
        # print(users)
        serializers = UserSerializer(users)
        return Response(serializers.data)