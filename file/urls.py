from django.urls import path
from .views import *

app_name='file'

urlpatterns=[
    path('index/',index,name='index')
]