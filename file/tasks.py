from __future__ import absolute_import,unicode_literals
import time
import os
from celery import shared_task

@shared_task
def add(x,y):
    return x+y