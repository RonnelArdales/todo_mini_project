from dataclasses import fields
from django import forms
from .models import Task


class TaskListForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'complete',)

