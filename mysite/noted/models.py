# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
import time

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

def file_path(instance,filename):
    tmp = instance.upload_date
    str(tmp)
    tmp = tmp.strftime('%Y-%m-%dT%H:%M:%S')
    print('T IS BELOW')
    print(tmp)
    #print(type(tmp))
    path = 'noted/uploads/'+instance.file_name+'_'+tmp+'.pdf';
    print('PATH BELOW')
    print(path)
    return path

class UploadedFile(models.Model):
    file_name = models.CharField(max_length=200)
    upload_date = models.DateTimeField('date uploaded')
    file_contents = models.FileField(upload_to=file_path)

    def __str__(self):
        return self.file_name
    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=7)
