from __future__ import absolute_import,unicode_literals

from celery.app.base import Celery
from file.models import Filemodel
from celery.schedules import crontab
from django.utils import timezone

import celery
app=Celery()

@app.on_after_configure.connect
def deleted_old_files(fayl,**kwargs):    
    fayllar = Filemodel.objects.all()

    # Iterate through them
    for fayl in fayllar:
        if fayl.expiration_date < timezone.now():
            fayl.delete()
            return "completed deleting foos at {}".format(timezone.now())