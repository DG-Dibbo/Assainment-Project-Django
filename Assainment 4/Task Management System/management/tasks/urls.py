from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_tasks,name='add_tasks'),
    path('edit/<int:task_id>/', views.edit_tasks, name='edit_tasks'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
]