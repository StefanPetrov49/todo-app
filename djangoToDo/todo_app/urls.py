from django.urls import path

from djangoToDo.todo_app.views import index, add_task

urlpatterns = (
    path('', index, name='index'),
    path('add/task/', add_task, name='add task'),
)