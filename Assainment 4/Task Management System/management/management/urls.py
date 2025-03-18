from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.management_system,name='management_system'),
    path('tasks/', include('tasks.urls')),
    path('categories/', include('categories.urls')),
]
