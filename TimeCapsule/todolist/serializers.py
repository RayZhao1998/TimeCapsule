from django.contrib.auth.models import User, Group
from rest_framework import serializers
from todolist.models import Task

class TodolistSerializers(serializers.HyperlinkedModelSerializer):
    task_title = serializers.CharField(max_length=128)
    task_isCompleted = serializers.CharField(max_length=1, default='0')
    task_priority = serializers.CharField(max_length=1, default='0')

    def create(self, validated_data):
        return Todolist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.task_title = validated_data.get('task_title', instance.task_title)
        instance.task_isCompleted = validated_data.get('task_isCompleted', instance.task_isCompleted)
        instance.task_priority = validated_data.get('task_priority', instance.task_priority)
        instance.save()
        return instance

    class Meta:
        model = Task
        fields = ('id', 'task_title', 'task_isCompleted', 'task_priority')
        
