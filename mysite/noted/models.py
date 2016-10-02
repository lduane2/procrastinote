# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
import time

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

def file_path(instance,filename):
    date = instance.upload_date
    str(date)
    date = date.strftime('%Y-%m-%dT%H%M%S')
    instance.stored_name = instance.file_name.replace(" ","_")+'_'+date
    instance.file_path = 'noted/uploads/'+instance.stored_name+'.pdf'
    return instance.file_path

class UploadedFile(models.Model):
    file_name = models.CharField(max_length=200)
    upload_date = models.DateTimeField(timezone.now())
    file_contents = models.FileField(upload_to=file_path)
    stored_name = models.CharField(max_length=300)
    file_path = models.CharField(max_length=400)

    def __str__(self):
        return self.file_name
