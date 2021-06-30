from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms #pour le register
from profil.models import *

class ChangeProfilForm(forms.ModelForm):
    class Meta:
        model = Winker
        fields = ['bio','etude','photoProfil']
    
    
class AddPictureWinkerForm(forms.ModelForm):
    class Meta:
        model = FilesWinker
        fields = ['image']

class CreateEventForm1(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['titre','bioEvent','dateFin','dateDebut']
        #exclude = ['dateDebut','creatorWinker','participeWinker']

class CreateEventForm2(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['ageMinimum','ageMaximum','localisation','hastags']

class AddMessageEventRamener(forms.ModelForm):
    class Meta:
        model = RamenerEvent
        fields = ['message']

# widgets = {
#             'username' : forms.TextInput(attrs={'class':'form-control' , 'placeholder': 'this is the username'}),
#             'password1' : forms.TextInput(attrs={'class':'form-control'}),
#         }
