from django import forms

from djangoToDo.todo_app.models import Task


class TaskModel(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'author', 'description']
        labels = {
            'title': 'Title',
            'author': 'Author',
            'description': 'Description',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title...'
                },
            ),
            'author': forms.TextInput(
                attrs={
                    'placeholder': 'Author...'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description...'
                }
            ),
        }


class EditTaskModel(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'author', 'description', 'completed']


class SearchForm(forms.Form):
    task_title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by title...'
            }
        ),
        label='',
    )