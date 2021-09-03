from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    username=models.CharField(('username'),max_length=30,null=True,unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_active = models.BooleanField(('active'), default=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name=('user')
        verbose_name_plural=('users')

    def get_full_name(self):
        full_name = '{}{} ' .format(self.first_name, self.last_name)
        return full_name.strip()
