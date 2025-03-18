from django import forms
from .models import Task_Model
from categories.models import Category_Model

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task_Model
        fields = '__all__'
        
    categories = forms.ModelMultipleChoiceField(
        queryset=Category_Model.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    
