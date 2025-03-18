from django import forms
from . import models

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category_Model
        fields = '__all__'