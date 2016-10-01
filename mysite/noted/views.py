# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import FileForm

from .models import UploadedFile

def index(request):
    latest_uploads_list = UploadedFile.objects.order_by('-upload_date')[:5]
    context = {
        'latest_uploads_list': latest_uploads_list,
    }
    return render(request, 'noted/index.html', context)

def detail(request,upload_id):
    upload = get_object_or_404(UploadedFile, pk=upload_id)
    return render(request, 'noted/detail.html', {'upload': upload})

def upload_file(request):
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			#handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect('noted/')
	else:
		form = FileForm()
	return render(request, 'noted/upload.html', {'form': form})