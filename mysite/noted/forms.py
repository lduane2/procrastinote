from django import forms
from django.utils import timezone

class ModelForm(forms.Form):
    file_name = forms.CharField(max_length=200)
    file_contents = forms.FileField()
