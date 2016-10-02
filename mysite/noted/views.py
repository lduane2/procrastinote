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
    filetext=[]
    contents=[]
    wavstr=""
    upload = get_object_or_404(UploadedFile, pk=upload_id)
    uf = UploadedFile.objects.raw('SELECT * FROM noted_uploadedfile WHERE id='+upload_id)
    if request.method == 'POST':
        mode = -1
        keyword=""
        if request.POST.get("keyword",""):
            keyword = request.POST.get("keyword","")
            if request.POST.get("sentence",""):
                mode = 0
            elif request.POST.get("paragraph",""):
                mode = 2
            elif request.POST.get("smart-paragraph",""):
                mode = 3
        elif request.POST.get("auto", ""):
            mode = 1

        if request.POST.get("reset",""):
            with open(uf[0].file_path, 'r') as document:
                config = {'conversion_target': DocumentConversionV1.NORMALIZED_HTML}
                response = document_conversion.convert_document(document=document, config=config).content
                try:
                    m = re.search('<body>(.*)</body>', response)
                    contents = m.group(1)
                except:
                    contents = response
        else:
            consolidate(mode=mode,keyword=keyword)
            with open('noted/pythonScripts/consolidate.txt', 'r') as document:
                contents=document.read().replace('\n', '')

        if request.POST.get("audio",""):
            wavstr = uf[0].folder
            wavstr = wavstr.split('/')[-2] + '.wav'
            speak(filename=wavstr)

    else:
        with open(uf[0].file_path, 'r') as document:
            config = {'conversion_target': DocumentConversionV1.NORMALIZED_HTML}
            response = document_conversion.convert_document(document=document, config=config).content
            try:
                m = re.search('<body>(.*)</body>', response)
                contents = m.group(1)
            except:
                contents = response

        tigers(filename=uf[0].file_path)

    keyconcepts()
    f1 = open('noted/pythonScripts/concepts.txt', 'r')
    for line in f1:
        filetext.append(line[:-1])

    return render(request, 'noted/detail.html', { 'contents': contents, 'upload': upload, 'filetext': filetext, 'wavFile': wavstr} )

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.upload_date = timezone.now()
            post.save()
            return HttpResponseRedirect('/noted/'+str(post.id)+'/')
        else:
            print form.errors
    else:
        form = UploadFileForm()
    return render(request, 'noted/upload.html',{ 'form': form })
