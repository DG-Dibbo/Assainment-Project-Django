from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician
from django.http import Http404

def musician_form(request):   
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('musician_form')
    else:
        form = MusicianForm()
    return render(request, 'mus_forms.html', {'form': form})



def musician_detail_view(request, id):
    try:
        mus_model = Musician.objects.get(pk=id)  
    except Musician.DoesNotExist:
        raise Http404("Musician not found")

    mus_form = MusicianForm(instance=mus_model)

    if request.method == 'POST':
        mus_form = MusicianForm(request.POST, instance=mus_model)
        if mus_form.is_valid():
            mus_form.save()
            return redirect('MusiciansDirectory')

    return render(request, 'mus_forms.html', {'form': mus_form})
