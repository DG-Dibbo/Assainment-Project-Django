from django.shortcuts import render, redirect
from . import forms
from Album.models import Album
from musician.models import Musician

from . import models

def album_view(request):
    album_sets = Album.objects.all() 

    if request.method == 'POST':
        selected_album = request.POST.get('album')
        if selected_album:
            selected_album = Album.objects.get(id=selected_album)
            formatted_date = selected_album.release_date.strftime('%Y-%m-%d %I:%M:%S %p')
            print(f"Selected Album: {selected_album.album_name}")

   
        musician_album = forms.ViewForm(request.POST)
        if musician_album.is_valid():
            email = musician_album.cleaned_data.get('email')
            if Musician.objects.filter(email = email).exists():
                musician_album.save() 
                print(musician_album.cleaned_data)
                return redirect('MusiciansDirectory') 
    else:
        musician_album = forms.ViewForm()

    return render(request, 'index.html', {'album_sets': album_sets, 'musician_album': musician_album})

def edit_album(request, id):
    album_sets = Album.objects.all() 
    album_instance = models.Album_View.objects.get(pk=id) 
    edit_form = forms.ViewForm(instance=album_instance)

    if request.method == 'POST':
        edit_form = forms.ViewForm(request.POST, instance=album_instance)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('MusiciansDirectory')

    return render(request, 'album_edit.html', {'edit_form': edit_form,'album_sets': album_sets,})

def delete_album(request,id):
    delete = models.Album_View.objects.get(pk=id)
    delete.delete()
    return redirect('MusiciansDirectory')