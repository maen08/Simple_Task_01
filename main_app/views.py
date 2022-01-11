from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import TaskSerializer
from rest_framework.response import Response

class TaskView(viewsets.ViewSet):
    def create(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    
    def retrieve(self,request):
        