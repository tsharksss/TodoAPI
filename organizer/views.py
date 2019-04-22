from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Task
from .serializers import TaskSerializers


class TaskListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    def post(self, request):
        task = TaskSerializers(data=request.data)
        if task.is_valid():
            task.save()
            return Response({'status': 'Success'})
        else:
            return Response({'status': 'Error'})


def updateTask(request):
    task = Task.objects.get(id=request.GET['update_id'])
    if task:
        task.text = request.GET['update_text']
        task.save()
        return HttpResponse('Success!')
    else:
        return HttpResponse('Error!')


def deleteTask(request):
    task = Task.objects.filter(id=request.GET['delete_id'])
    if task:
        task.delete()
        return HttpResponse('Success!')
    else:
        return HttpResponse('Error!')
