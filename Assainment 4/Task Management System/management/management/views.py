from django.shortcuts import render
from tasks.models import Task_Model

def management_system(request):
    tasks = Task_Model.objects.all() 
    return render(request, 'index.html', {'data': tasks})
