from django import forms
from django.utils import timezone

class ModelForm(forms.Form):
    file_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
    file_contents = forms.FileField()
    #data above accessible by request.FILES['file']
