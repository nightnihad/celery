from user.forms import LoginForm
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

app_name='user'

urlpatterns=[
    path('', login_required(TemplateView.as_view(template_name="main.html")),name='main'),
    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('profil/',views.profil,name='profil'),
    path('file/<str:id>',views.allowed,name='file'),
    path('myfiles/',views.myfiles,name='myfiles')
]