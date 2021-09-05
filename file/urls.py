from django.urls import path
from .views import *

app_name='file'

urlpatterns=[
    path('update/<str:id>',updatefile,name='updatefile'),
    path('delete/<str:id>',deletefile,name='deletefile'),
    path('detail/<str:id>',addcomment,name='detail'),
    path('deletecomment/<str:id>',deletecomment,name='deletecomment'),
    path('newfile/',savefile,name='savefile'),
    path('deleteshared/<str:id>/',deleteshared,name='deleteshared'),
]