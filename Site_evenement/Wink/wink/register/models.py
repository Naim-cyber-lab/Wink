from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.
# class IntegerRangeField(models.IntegerField):
#     def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
#         self.min_value, self.max_value = min_value, max_value
#         models.IntegerField.__init__(self, verbose_name, name, **kwargs)
#     def formfield(self, **kwargs):
#         defaults = {'min_value': self.min_value, 'max_value':self.max_value}
#         defaults.update(kwargs)
#         return super(IntegerRangeField, self).formfield(**defaults)

# class Client(models.Model):
#     adresse = models.CharField(max_length=255)

# class Winker(AbstractUser):
#     birth = models.DateField(null=True)
#     photoProfil = models.ImageField(upload_to="pics",null=True,blank=True)
#     sexe = models.CharField(max_length=30,null=True)
#     etude = models.CharField(max_length=250,blank=True,null=True)
#     bio = RichTextField(blank=True,null=True)

# class FilesWinker(models.Model):
#     winker = models.ForeignKey(Winker, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(null=True)

# class Event(models.Model):
#     creatorWinker = models.ForeignKey(Winker, on_delete=models.CASCADE, null=True,blank=True)
#     titre = models.CharField(max_length=30)
#     dateDebut = models.DateField(null=True)
#     dateFin = models.DateField(null=True)
#     datePublication = models.DateField(default=datetime.date.today)
#     adresse = models.CharField(max_length=255,null=True)
#     localisation = models.CharField(max_length=255,null=True)
#     hastags = models.CharField(max_length=150,null=True)
#     ageMinimum = models.IntegerField(default = 0)
#     ageMaximum = models.IntegerField(default = 125)
#     accessTous = models.BooleanField(default = True)
#     accessFollow = models.BooleanField(default = False)
#     accessFollower = models.BooleanField(default = False)
#     bioEvent = RichTextField(blank=True,null=True)
#     moyenneAge = models.IntegerField(null=True)
#     nbFille = models.IntegerField(null=True)
#     nbGarcon = models.IntegerField(null=True)
#     attenteWinker = models.ManyToManyField(Winker,related_name="attenteEvent", blank=True)
#     participeWinker = models.ManyToManyField(Winker,related_name="participeEvent",blank=True)
#     nbLike = models.IntegerField(default=0)
#     nbHaha = models.IntegerField(default=0)
#     nbLove = models.IntegerField(default=0)
#     nbAngry = models.IntegerField(default=0)
#     nbSad = models.IntegerField(default=0)
#     nbWow = models.IntegerField(default=0)

# class SignalerArticle(models.Model):
#     winkerSignalement = models.ForeignKey(Winker, on_delete=models.CASCADE, null=True )
#     eventSignalement = models.ForeignKey(Event, on_delete=models.CASCADE, null=True )
#     raisonSignalement = models.CharField(max_length=255, null=True, blank=True)

# class ReactionEvent(models.Model):
#     winkerReaction = models.ForeignKey(Winker, on_delete=models.CASCADE, null=True )
#     eventReaction = models.ForeignKey(Event, on_delete=models.CASCADE, null=True )
#     reaction = models.IntegerField() # -1 POUR UN ANGRY / 1 POUR UN LIKE / 2 POUR HAHA / 3 POUR WAW / 4 POUR SAD / 5 POUR LOVE
   
# class RamenerEvent(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
#     message = models.CharField(max_length=255)
#     fait = models.BooleanField(default=False)
#     date = models.DateField(default=datetime.date.today)
    

# class FilesEvent(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(null=True)

# class NotePlayer(models.Model):
#     winker = models.ForeignKey(Winker, on_delete=models.CASCADE, null=True,blank=True)
#     note = IntegerRangeField(min_value=0, max_value=5)

# class PublicChatRoom(models.Model):
#     users = models.ManyToManyField(Winker,help_text="users who are connected to the chat")

#     def connect_user(self,user):
#         """
#         méthode d'instance
#         return True if user is added to the users list
#         """

#         is_user_added = False
#         if not user in self.users.all():
#             self.users.add(user)
#             self.save()
#             is_user_added = True
#         elif user in self.users.all():
#             is_user_added = True
#         return is_user_added

#     def disconnect_user(self,user):
#         """
#         méthode d'instance
#         return True if user is added to the users list
#         """

#         is_user_removed = False
#         if not user in self.users.all():
#             self.users.remove(user)
#             self.save()
#             is_user_removed = True
#         return is_user_removed

#     @property
#     def group_name(self):
#         """
#         Returns the channels group that sockets
#         should subscribe to and get sent messages as they are generated
#         """

#         return f"PublicComment-{self.id}"


# class PublicChatRoomMessage(models.Model):
#     winkerComment = models.ForeignKey(Winker, on_delete=models.CASCADE, null=True )
#     eventComment = models.ForeignKey(Event, on_delete=models.CASCADE, null=True )
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add = True)



