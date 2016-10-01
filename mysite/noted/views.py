# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

import re
import json
import os
from os.path import join, dirname
from watson_developer_cloud import DocumentConversionV1

from .forms import ModelForm
from .models import UploadedFile

from django.utils import timezone


document_conversion = DocumentConversionV1(
                                           username='632d20d2-21d6-4b72-b1e4-35409db12fe3',
                                           password='nB2m1r40gUIi',
                                           version='2016-02-09')

def index(request):
    uploads_list = UploadedFile.objects.order_by('-upload_date')
    context = {
            'uploads_list': uploads_list,
            }
    return render(request, 'noted/index.html', context)

def list(request):
    uploads_list = UploadedFile.objects.order_by('-upload_date')
    context = {
            'uploads_list': uploads_list,
            }
    return render(request, 'noted/list.html', context)

def detail(request,upload_id):
    name_map = { 'name': 'file_name', 'date': 'upload_date' }
    results = UploadedFile.objects.raw('SELECT * FROM noted_uploadedfile WHERE ID='+upload_id,translations=name_map)
    tmp = results['date']
    str(tmp)
    tmp = tmp.strftime('%Y-%m-%dT%H:%M:%S')
    path = 'noted/uploads/'+results['name']+'_'+tmp+'.pdf';
    print('YA PATH')
    print(path)

    upload = get_object_or_404(UploadedFile, pk=upload_id)
    with open('noted/uploads/Fall_2016_Resume.pdf', 'r') as document:
        config = {'conversion_target': DocumentConversionV1.NORMALIZED_HTML}
        response = document_conversion.convert_document(document=document, config=config).content
        m = re.search('<body>(.*)</body>', response)
        found = m.group(1)
    return render(request, 'noted/detail.html', {'found': found, 'upload': upload} )

def upload_file(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.upload_date = timezone.now()
            print form['file_name']
            form.save()
            return HttpResponseRedirect('noted/list/')
    else:
        form = ModelForm()
    return render(request, 'noted/upload.html', {'form': form})
