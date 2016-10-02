from django import forms
from django.utils import timezone

from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        exclude = ['upload_date','file_path','folder']
    file_name = forms.CharField(max_length=200)
    file_contents = forms.FileField()

<<<<<<< HEAD
#class Form(forms.Form):
   # haha = 'lol'
=======
>>>>>>> cd24d4dad7c9b824ec5114c122b23516598a7713
