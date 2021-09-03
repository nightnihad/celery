from __future__ import absolute_import, unicode_literals
from datetime import datetime, timedelta
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','filesharer.settings')
app=Celery('filesharer')



app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone='Asia/Baku'

app.autodiscover_tasks()

