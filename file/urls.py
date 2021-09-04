from django.urls import path
from .views import *

app_name='file'

urlpatterns=[
    path('update/<str:id>',updatefile,name='updatefile'),
    path('delete/<str:id>',deletefile,name='deletefile'),
    path('detail/<str:id>',addcomment,name='detail')
]