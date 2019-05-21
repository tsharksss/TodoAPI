from django.urls import path

from .views import TaskListView, updateTask, deleteTask

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('delete/', deleteTask, name='delete-task'),
    path('update/', updateTask, name='update-task'),
]
