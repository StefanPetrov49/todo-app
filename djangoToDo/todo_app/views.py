from django.shortcuts import render, redirect

from djangoToDo.todo_app.forms import TaskModel
from djangoToDo.todo_app.models import Task


# Create your views here.

def index(request):
    all_tasks = Task.objects.all()

    context = {
        'all_tasks': all_tasks,
    }

    return render(request, 'index.html', context)

def add_task(request):

    if request.method == 'GET':
        form = TaskModel()
    else:
        form = TaskModel(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'add-task.html', context)