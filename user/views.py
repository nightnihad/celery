from django.core.exceptions import ValidationError
from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .forms import AllowerForm, RegisterForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from file.models import ShareModel,Filemodel,CommentModel
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
def logout(request):
    auth_logout(request)
    messages.success(request,'Çıxış etdiniz',)
    return redirect('/')
def profil(request):
    userinformation=CustomUser.objects.get(username=request.user)
    allowedinformation=ShareModel.objects.filter(sender=request.user)
    allowerinformation=ShareModel.objects.filter(receiver=request.user)
    context={
        'userinformation':userinformation,
        'allowedinformation':allowedinformation,
        'allowerinformation':allowerinformation
    }
    return render(request,'profil.html',context)
def allowed(request):
    form=AllowerForm()
    context={
        'form':form
    }
    if request.method=='POST':
        form=AllowerForm(request.POST,request.FILES)
        if form.is_valid():
            sender=request.user
            receiver=form.cleaned_data.get('receiver')
            file=form.cleaned_data.get('file')
            see_comments=form.cleaned_data.get('see_comments')
            user2=CustomUser.objects.get(Q(username=receiver) | Q(email=receiver))
            if user2 is None:
                return render(request,'allowed.html',context)
            if request.user.username ==receiver or request.user.email==receiver:
                raise ValidationError('salam qaqa')
            newallowed=ShareModel.objects.create(sender=sender,file=file,receiver=receiver,see_comments=see_comments)
            newallowed.save()
            return redirect('/')
        return render(request,'allowed.html',context)
    return render(request,'allowed.html',context)
            