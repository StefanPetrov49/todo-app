from django.urls import path

from djangoToDo.todo_app.views import index, add_task, edit_task, complete_task, completed_tasks, details_task

urlpatterns = (
    path('', index, name='index'),
    path('completed/', completed_tasks, name='completed_tasks'),
    path('add/task/', add_task, name='add task'),
    path('edit/task/<int:task_id>', edit_task, name='edit task'),
    path('details/task/<int:task_id>', details_task, name='details task'),
    path('complete/task/<int:task_id>', complete_task, name='complete task'),
)