from logging import FATAL
from django.db import models
from datetime import datetime, timedelta, timezone
from django.db.models.deletion import CASCADE
from user.models import CustomUser
# Create your models here.
"""Fayl modeli yaradılır və özəllikləri qeyd edilir."""
class Filemodel(models.Model):
    author=models.ForeignKey(CustomUser,related_name='users',verbose_name='Yazar',on_delete=models.CASCADE)
    name=models.CharField(max_length=50,verbose_name='Ad')
    description=models.TextField(null=True,blank=False,verbose_name='Açıqlama')
    file=models.FileField(upload_to='files',verbose_name='Fayl',null=False,blank=False)
    created_date=models.DateTimeField()
    update_date=models.DateTimeField()
    expiration_date = models.DateTimeField()
    
    def __str__(self):
        return self.name


    """Yaranma və dəyişdirilmə tarixi üçün save metodunu override"""
    def save(self,*args,**kwargs):
        if not self.id:
            self.created_date=datetime.now()
        self.update_date=datetime.now()
        return super(Filemodel, self).save(*args,**kwargs)



class CommentModel(models.Model):
    author=models.ForeignKey(CustomUser,verbose_name='Yazar', on_delete=models.CASCADE)
    content=models.TextField(verbose_name='Mezmun',null=False, blank=False)
    comment_date=models.DateTimeField(auto_now_add=True,verbose_name='Yazilma Tarixi')
    file = models.ForeignKey(Filemodel,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.content


class ShareModel(models.Model):
    file=models.ForeignKey(Filemodel,related_name='shared_files',on_delete=models.DO_NOTHING)
    sender=models.ForeignKey(CustomUser,related_name='gonderen',on_delete=models.DO_NOTHING)
    receiver=models.CharField(max_length=50,verbose_name='Alıcı',null=True)
    see_comments=models.BooleanField(default=False)

    def __str__(self):
        return self.file

