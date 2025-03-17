from django.shortcuts import render,redirect
from . import forms

def add_album(request):
    if request.method == 'POST':
        album = forms.AlbumForm(request.POST)
        if album.is_valid():
            album.save()
            return redirect('add_album')
    else:
        album = forms.AlbumForm()
    return render(request,'add_album.html',{'form' : album})