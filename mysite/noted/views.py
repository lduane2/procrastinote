# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import UploadedFile

def index(request):
    latest_uploads_list = UploadedFile.objects.order_by('-upload_date')[:5]
    context = {
        'latest_uploads_list': latest_uploads_list,
    }
    return render(request, 'noted/index.html', context)

def detail(request,upload_id):
    uf = get_object_or_404(File, pk=upload_id)
    return render(request, 'noted/detail.html', {'upload': uf})

def upload(request):
    context = {}