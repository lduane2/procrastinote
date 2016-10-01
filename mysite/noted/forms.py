from django import forms

class ModelFormWithFileField(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    #data above accessible by request.FILES['file']

