from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django import utils
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, date, time, timedelta
from .tasks import deleted_old_files
from .models import *
from user.models import CustomUser
# Create your views here.

def savefile(request):
    form=FileForm()
    context={'form':form}
    if request.method=='POST':
        form=FileForm(request.POST,request.FILES)
        if form.is_valid():
            fayl=form.save(commit=False)
            fayl.author=request.user
            fayl.expiration_date=utils.timezone.now()+ timedelta(days=7)
            fayl.save()
            messages.success(request,'fayl yaradıldı')
            return redirect('file:detail',id=fayl.id)
    return render(request,'newfile.html',context)
"""def dashboard(request):
    fayllar=Filemodel.objects.all()
    user=request.user.username
    dashboarduser=CustomUser.objects.get(username=user)
    context={
        'fayllar':fayllar,
        'dashboarduser':dashboarduser
    }

    return render(request,'profil.html')"""
@login_required()
def updatefile(request,id):
    sifaris=Filemodel.objects.get(id=id)
    formupdate1=UpdateForm(instance=sifaris)
    if request.method =='POST':
        formupdate1=UpdateForm(request.POST,request.FILES,instance=sifaris)
        if formupdate1.is_valid():
            formupdate1.save()
            messages.success(request,'dəyişikliklər edildi')
            return redirect('user:profil')
    context1={
    'formupdate1':formupdate1
    }
    return render(request,'update.html',context1)

@login_required()
def deletefile(request,id):
    sifaris=Filemodel.objects.get(id=id)
    context={
        'sifaris':sifaris
    }
    if request.method =='POST':
        sifaris.delete()
        messages.success(request,'fayl silindi')
        return redirect('user:profil')
    return render(request,'delete.html',context)
@login_required()
def addcomment(request,id):
    file= get_object_or_404(Filemodel,id=id)
    sharefile=file.shared_files.filter()
    form=CommentForm()
    comments=file.comments.all()
    context={
        'file':file,
        'form':form,
        'comments':comments,
        'sharefile':sharefile
    }
    if request.method=='POST':
        form=CommentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.file=file
            comment.save()
            messages.success(request, 'Yorum başarılı bir şekilde eklendi.')
            return redirect('file:detail',id=file.id)
    return render(request,'detail.html',context)
@login_required()
def deletecomment(request,id):
    comment=get_object_or_404(CommentModel,id=id)
    if request.user ==comment.author or request.user==comment.file.author:
        comment.delete()
        messages.success(request,'rəy silindi')
        return redirect('file:detail', id=comment.file.id)
    return HttpResponse('ancaq oz commentlerivi sile bilersen.bu commenti sile bilmezsen')
@login_required
def deleteshared(request,id):
    file=ShareModel.objects.get(id=id)
    file.delete()
    messages.success(request,'fayl silindi')
    return redirect('user:profil')

    