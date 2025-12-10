from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import MediaFile




class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2" ]



class MediaForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'file']


