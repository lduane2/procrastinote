# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import ModelFormWithFileField

from .models import UploadedFile

def index(request):
    latest_uploads_list = UploadedFile.objects.order_by('-upload_date')[:5]
    context = {
        'latest_uploads_list': latest_uploads_list,
    }
    return render(request, 'noted/index.html', context)

def detail(request,upload_id):
    uf = get_object_or_404(UploadedFile, pk=upload_id)
    return render(request, 'noted/detail.html', {'upload': uf})

def upload_file(request):
	if request.method == 'POST':
		form = ModelFormWithFileField(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			#handle_uploaded_file(request.FILES['file'])
			#my_model.save()
			return HttpResponseRedirect('noted/')
		else:
			form = ModelFormWithFileField()
		return render(request, 'upload.html', {'form': form})