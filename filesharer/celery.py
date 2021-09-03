from __future__ import absolute_import, unicode_literals
from datetime import datetime, timedelta
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','filesharer.settings')
app=Celery('filesharer')
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'


app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone='Asia/Baku'

app.autodiscover_tasks()

