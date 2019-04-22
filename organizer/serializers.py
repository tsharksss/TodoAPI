from rest_framework import serializers

from .models import Task


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'text', 'pub_date', 'marked')


class DeleteTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = 'id'