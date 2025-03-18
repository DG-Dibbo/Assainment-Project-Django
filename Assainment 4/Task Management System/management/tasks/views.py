from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task_Model

def add_tasks(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.save()
            task_form.save_m2m()
            return redirect('management_system')
    else:
        task_form = TaskForm()
    
    return render(request, 'add_task.html', {'form': task_form})

def edit_tasks(request, task_id):
    task = Task_Model.objects.get(id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            form.save_m2m()
            return redirect('management_system')
    else:
        form = TaskForm(instance=task)

    return render(request, 'editor_task.html', {'form': form, 'task': task})

def delete_task(request, id):
    task = Task_Model.objects.get(pk=id)
    task.delete()
    return redirect('management_system')
