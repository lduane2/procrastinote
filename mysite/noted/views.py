# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone

import re
import json
import os
from os.path import join, dirname
from watson_developer_cloud import DocumentConversionV1

from .forms import UploadFileForm
from .models import UploadedFile

from .pythonScripts.tigersOO import tigers
from .pythonScripts.consolidateOO import consolidate
from .pythonScripts.keyconceptsOO import keyconcepts
from .pythonScripts.speakOO import speak

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
    if request.method == 'POST':
        print "posted"
    else:
        uf = UploadedFile.objects.raw('SELECT * FROM noted_uploadedfile WHERE id='+upload_id)
        upload = get_object_or_404(UploadedFile, pk=upload_id)
        with open(uf[0].file_path, 'r') as document:
            config = {'conversion_target': DocumentConversionV1.NORMALIZED_HTML}
            response = document_conversion.convert_document(document=document, config=config).content
            try:
                m = re.search('<body>(.*)</body>', response)
                found = m.group(1)
            except:
                found = response
        tigers(filename=uf[0].file_path)
        keyconcepts()
        f1 = open('noted/pythonScripts/concepts.txt', 'r')
        fileText=[]
        for line in f1:
            fileText.append(line[:-1])
    wavstr = uf[0].folder
    wavstr = wavstr.split('/')[-2] + '.wav'
    consolidate()
    speak(filename=wavstr)
    return render(request, 'noted/detail.html', { 'found': found, 'upload': upload, 'fileText': fileText, 'wavFile': '../media/'+wavstr} )

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            print "Valid form :)"
            post = form.save(commit=False)
            post.upload_date = timezone.now()
            post.save()
            return HttpResponseRedirect('/noted/'+str(post.id)+'/')
        else:
            print form.errors
    else:
        form = UploadFileForm()
    return render(request, 'noted/upload.html',{ 'form': form })


