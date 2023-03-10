from django.shortcuts import render, redirect

from djangoToDo.todo_app.forms import TaskModel, EditTaskModel, SearchForm
from djangoToDo.todo_app.models import Task


# Create your views here.

def index(request):
    search_form = SearchForm()
    all_tasks = Task.objects.filter(completed=False)

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_tasks = all_tasks.filter(title__icontains=search_form.cleaned_data['task_title'])

    context = {
        'all_tasks': all_tasks,
        'search_form': search_form,
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


def edit_task(request, task_id):
    task = Task.objects.filter(pk=task_id).get()
    if request.method == "GET":
        form = EditTaskModel(instance=task)
    else:
        form = EditTaskModel(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {
        'form': form,
        'task_id': task_id,
    }

    return render(request, 'edit-task.html', context)


def complete_task(request, task_id):
    task = Task.objects.filter(pk=task_id).get()
    if task.completed:
        task.completed = False
    else:
        task.completed = True

    task.save()
    redirect_path = request.META['HTTP_REFERER']
    return redirect(redirect_path)

def completed_tasks(request):
    all_tasks = Task.objects.filter(completed=True)
    context = {
        'all_tasks': all_tasks,
    }
    return render(request, 'completed-tasks.html', context)
