from django.db import models
from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    field = '__all__'
    model = Task