from django import forms

from djangoToDo.todo_app.models import Task


class TaskModel(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'author', 'description']