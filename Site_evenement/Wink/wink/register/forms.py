from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms #pour le register
from profil.models import User
from profil.models import Winker

class RegisterForm(UserCreationForm):
    class Meta:
        model = Winker
        fields = ['username', 'password1', 'password2']

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control' , 'placeholder': 'this is the username'}),
            'password1' : forms.TextInput(attrs={'class':'form-control'}),
        }