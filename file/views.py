from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
import datetime
from django.contrib import messages

from .tasks import delete_old_files
from .models import *
from user.models import CustomUser
# Create your views here.

def saveform(request):
    form=FileForm()
    if request.method=='POST':
        form=FileForm(request.POST)
        if form.is_valid():
            fayl=form.save(commit=False)
            fayl.author=request.user.username
            fayl.expiration_date=timezone.now() + datetime.timedelta(days=7)
            fayl.save()
            delete_old_files.delay(fayl)
            return redirect()
    return render()
"""def dashboard(request):
    fayllar=Filemodel.objects.all()
    user=request.user.username
    dashboarduser=CustomUser.objects.get(username=user)
    context={
        'fayllar':fayllar,
        'dashboarduser':dashboarduser
    }

    return render(request,'profil.html')"""
def allowedperson(request,id):
    return render()
def updatefile(request,id):
    sifaris=Filemodel.objects.get(id=id)
    formupdate1=FileForm(instance=sifaris)
    if request.method =='POST':
        formupdate1=FileForm(request.POST,request.FILES,instance=sifaris)
        if formupdate1.is_valid():
            formupdate1.save()
            messages.success(request,'dəyişikliklər edildi')
            return redirect('user:profil')
    context1={
    'formupdate1':formupdate1
    }
    return render(request,'update.html',context1)

def deletefile(request,id):
    sifaris=Filemodel.objects.get(id=id)
    context={
        'sifaris':sifaris
    }
    if request.method =='POST':
        sifaris.delete()
        return redirect('user:profil')
    return render(request,'delete.html',context)
def addcomment(request,id):
    file= get_object_or_404(Filemodel,id=id)
    form=CommentForm()
    comment1=get_object_or_404(CommentModel,file=file)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.file=file
            comment.save()
            messages.success(request, 'Yorum başarılı bir şekilde eklendi.')
            return redirect('/')
    context={
        'file':file,
        'form':form,
        'comment1':comment1
    }
    return render(request,'detail.html',context)
def deletecomment(request,id):
    file=get_object_or_404(Filemodel,id=id)
    comment=get_object_or_404(CommentModel,file=file)
    if request.method=='POST':
        comment.delete()
        return redirect('/')
    return render(request,'deletecomment.html',{'comment':comment})