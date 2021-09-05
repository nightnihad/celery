from user.forms import LoginForm
from django.urls import path
from . import views

app_name='user'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('profil/',views.profil,name='profil'),
    path('file/<str:id>',views.allowed,name='file'),
    path('myfiles/',views.myfiles,name='myfiles')
]