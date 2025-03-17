from django.shortcuts import render 
from album_manager.models import Album_View
from musician.models import Musician

def MusiciansDirectory(request): 
    std = Album_View.objects.all()
    return render(request, 'home.html',{'std':std}) 


