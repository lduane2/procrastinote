# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class UploadedFile(models.Model):
    file_name = models.CharField(max_length=200)
    upload_date = models.DateTimeField('date uploaded')
    file_contents = models.FileField(upload_to='noted/uploads')

    def __str__(self):
        return self.file_name
    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=7)
