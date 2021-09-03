from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
class RegisterForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','email','password1','password2','avatar']
        widgets = {
        'first_name': forms.fields.TextInput(attrs={'placeholder': 'first_name'}),

        'username': forms.fields.TextInput(attrs={'placeholder': 'last_name'}),

        'username': forms.fields.TextInput(attrs={'placeholder': 'username'}),

        'email': forms.fields.TextInput(attrs={'placeholder': 'email stuff'})
        }