# Musicians_Directory/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MusiciansDirectory, name='MusiciansDirectory'),
    path('musician/', include('musician.urls')),
    path('album/', include('Album.urls')),
    path('album_viewer/', include('album_manager.urls')), 
]
