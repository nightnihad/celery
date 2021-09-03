from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logout

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    form=RegisterForm()
    context={
        'form':form
    }
    if request.method=='POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            avatar=form.cleaned_data.get('avatar')
            username = form.cleaned_data.get("username")
            password1= form.cleaned_data.get("password1")
            email=form.cleaned_data.get('email')
            newUser =CustomUser(username =username,email=email,first_name=first_name,last_name=last_name)
            newUser.set_password(password1)
            newUser.save()
            auth_login(request,newUser)
            return redirect('/')
        messages.success(request,'Qeyd olunmadınız')
        return render(request,'register.html',context)
    return render(request,'register.html',context)

def login(request):
    if request.user.is_authenticated:
        return render('/')
    form=LoginForm()
    context={
        'form':form
    }
    if request.method =='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')
            user1=authenticate(username=username,password=password,email=email)
            if user1 is None:
                return render(request,'login.html',context)
            auth_login(request,user1)
            messages.success(request,'Qeyd olundunuz')
            return redirect('/')
    return render(request,'login.html',context)
