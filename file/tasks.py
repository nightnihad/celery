from __future__ import absolute_import,unicode_literals
from file.models import Filemodel

from celery.schedules import crontab
from django.utils import timezone

import celery

@celery.decorators.periodic_task(run_every=crontab(minute='*/5'))
def delete_old_files(fayl):
    if fayl.expiration_date < timezone.now():
        fayl.delete()
            # log deletion
        return "completed deleting foos at {}".format(timezone.now())