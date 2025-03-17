from django import forms
from .models import Album_View

class ViewForm(forms.ModelForm):
    class Meta:
        model = Album_View
        fields = '__all__'