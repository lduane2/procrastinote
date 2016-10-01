from django import forms
from django.utils import timezone

class ModelForm(forms.Form):
    file_name = forms.CharField(max_length=200)
    upload_date = forms.DateTimeField(timezone.now())
    file_contents = forms.FileField()
    #data above accessible by request.FILES['file']
