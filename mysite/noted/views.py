# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm

from .models import UploadedFile


def index(request):
    latest_uploads_list = UploadedFile.objects.order_by('-upload_date')[:5]
    context = {
        'latest_uploads_list': latest_uploads_list,
    }
    return render(request, 'noted/index.html',context)

def detail(request,upload_id):
    f = get_object_or_404(File, pk=upload_id)
    return render(request, 'noted/detail.html', {'upload': upload})

def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect('noted/uploaded/')
		else:
			form = UploadFileForm()
		return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
	with open('./uploadedFiles/tmp', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

