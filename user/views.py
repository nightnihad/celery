from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logout

# Create your views here.
def register(request):
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
    
