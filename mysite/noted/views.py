# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import ModelForm

from .models import UploadedFile

def index(request):
    uploads_list = UploadedFile.objects.order_by('-upload_date')
    context = {
            'uploads_list': uploads_list,
            }
    return render(request, 'noted/index.html', context)

def detail(request,upload_id):
    upload = get_object_or_404(UploadedFile, pk=upload_id)
    return render(request, 'noted/detail.html', {'upload': upload})

def list(request):
    uploads_list = UploadedFile.objects.order_by('-upload_date')
    context = {
            'uploads_list': uploads_list,
            }
    return render(request, 'noted/list.html', context)

def upload_file(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                #handle_uploaded_file(request.FILES['file'])
                return HttpResponseRedirect('noted/')
            except:
                return HttpResponseRedirect('upload/')
    else:
        form = ModelForm()
    return render(request, 'noted/upload.html', {'form': form})
