from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import TaskListForm, TaskUpdateForm
from .models import Task, User
from django.contrib import messages
# Create your views here.\
@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)

    return render(request, 'dashboard/home.html', {'tasks' : tasks})

@login_required
def addtask(request):
    if request.POST:
        form = TaskListForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskListForm()

    return render(request, 'dashboard/addtask.html', {'form':form})

@login_required
def taskview(request, pk):
    task = get_object_or_404(Task, pk=pk)

    return render (request, 'dashboard/taskview.html', {"task":task})

@login_required
def taskupdate(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.POST:
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskUpdateForm(instance=task)

    return render(request, 'dashboard/taskupdate.html', {"form": form})

@login_required
def taskdelete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    
    return redirect('home')    