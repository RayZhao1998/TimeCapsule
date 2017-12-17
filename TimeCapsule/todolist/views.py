# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from models import Task
from todolist.serializers import TodolistSerializers

# Create my views start #

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def get_todolist(request):
    if request.method == 'GET':
        todolist = Task.objects.all()
        serializer = TodolistSerializers(todolist, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        task_title = request.POST["title"]
        task_isCompleted = '0'
        task_priority = request.POST['task_priority']
        task = Task(task_title=task_title, task_isCompleted=task_isCompleted, task_priority=task_priority)
        task.save()
        todolist = Task.objects.all()
        todolist = todolists.order_by("-id")
        serializer = TodolistSerializers(todolist, many=True)
        return JSONResponse(serializer.data)
    else:
        todolist = Task.objects.all()
        serializer = TodolistSerializers(todolist, many=True)
        return JSONResponse(serializer.data)

# Create my views end #
