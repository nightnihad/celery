from django.shortcuts import render,redirect
from .forms import *
from datetime import datetime, timedelta,timezone


from .tasks import delete_old_files
from .models import *
from user.models import CustomUser
# Create your views here.
def index(request):
    form=ShareForm()
    return render(request,'index.html',{'form':form})
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
def dashboard(request):
    return render()
def allowedperson(request,id):
    return render()
def upgradefile(request,id):
    return render()

def deletefile(request,id):
    return render()


