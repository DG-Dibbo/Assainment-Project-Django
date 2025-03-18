from django.shortcuts import render,redirect
from . import forms
# Create your views here.

def add_categories(request):
    if request.method == 'POST':
        cat_form =  forms.CategoryForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            return redirect('add_categories')
    else:
        cat_form = forms.CategoryForm()
    return render(request,'add_category.html',{'form':cat_form})