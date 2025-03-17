from django.shortcuts import render
from . import forms
from . import models
# Create your views here.

# def forms_page(request):
#     if request.method == 'POST':
#         name = request.POST.get('username')
#         return render(request,'about.html',{'name':name})
     
#     return render(request,'forms.html')
def home(request):
    student = models.MyModel.objects.all()
    return render(request,'models.html',{'data':student})

def forms_page(request):
    if request.method == 'POST':
        form = forms.StudentForms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = forms.StudentForms()
    return render(request,'forms.html',{'form' : form})