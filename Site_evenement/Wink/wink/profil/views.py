from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from profil.forms import *

from django.contrib.auth.models import User
from profil.models import *

import datetime

from collections import Counter
from statistics import mean

from django.contrib.auth.decorators import login_required

from django.template.defaulttags import register
from django.forms import inlineformset_factory

from django.http import JsonResponse

#Creation de mes propres filtres
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
#{{ mydict|get_item:NAME }}

def from_dob_to_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

@login_required
def modifProfil(request):
    utilisateur = Winker.objects.get(id=request.user.id)
    user = request.user
    form = ChangeProfilForm(instance=user)
    FilesEventFormSet = inlineformset_factory(Winker, FilesWinker, fields=('image',))
    if request.method == 'POST':#modification du profil
        form = ChangeProfilForm(request.POST, request.FILES,instance=user)
        formFile = FilesEventFormSet(request.POST, request.FILES,instance=user)
        if form.is_valid():
            if formFile.is_valid():
                form.save()
                formFile.save()
            return redirect('/profil/modifProfil/') #page que l'on a pas encore crée
    
    return render(request,'modifProfil.html',{'FilesEventFormSet':FilesEventFormSet,'form':form,'utilisateur':utilisateur,'age':from_dob_to_age(utilisateur.birth)})

@login_required
def Profil(request):
    utilisateur = Winker.objects.get(id=request.user.id)

    ListIdEventParticipe = [Event.objects.get(id=x.id) for x in Event.objects.filter(creatorWinker=utilisateur.id)]
    for x in Event.objects.filter(participeWinker=utilisateur.id):
        ListIdEventParticipe.append(Event.objects.get(id=x.id))
    

    filesWinker = FilesWinker.objects.filter(winker=utilisateur.id)

    filesUser = FilesWinker.objects.filter(winker=utilisateur.id)

    return render(request,'Profil.html',{'utilisateur':utilisateur,
    'numberFiles':range(1,len(filesWinker)+2),
    'ListIdEventParticipe':ListIdEventParticipe,
    'filesUser':zip(filesUser,range(2,len(filesWinker)+2))
    })

@login_required
def NouvellePhoto(request):
    utilisateur = Winker.objects.get(id=request.user.id)
    user = request.user
    form = AddPictureWinkerForm(instance=user)

    filesWinker = FilesWinker.objects.filter(winker=utilisateur.id)
    ListFilesWinker = [x.image.url for x in filesWinker]
    numberFile = range(1,len(ListFilesWinker)+1)
    zipNumberFile = zip(numberFile,ListFilesWinker)

    if request.method == 'POST':#modification des photos
        form = AddPictureWinkerForm(request.POST, request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/profil/modifProfil/')


    return render(request,'NouvellePhoto.html',{'form':form, 'numberFile':numberFile,'zipNumberFile':zipNumberFile})

@login_required
def CreateEvent(request):
    utilisateur = Winker.objects.get(id=request.user.id)

    form1 = CreateEventForm1()
    form2= CreateEventForm2()
    FilesEventFormSet = inlineformset_factory(Event, FilesEvent, fields=('image',))
  
    if request.method == 'POST':
        form1 = CreateEventForm1(request.POST, request.FILES)
        form2 = CreateEventForm2(request.POST, request.FILES)
        if form1.is_valid():
            if form2.is_valid():
                obj1 = form1.save(commit=False)
                formFile = FilesEventFormSet(request.POST, request.FILES,instance=obj1)
                form2 = CreateEventForm2(request.POST, request.FILES,instance=obj1)
                if form2.is_valid():
                    if formFile.is_valid():

                        obj2 = form2.save(commit=False)
                        obj2.creatorWinker = utilisateur
                        obj1.save()
                        obj2.save()

                        formFile.save()


    return render(request,'CreateEvent.html',{
        'FilesEventFormSet':FilesEventFormSet,
        # 'formFile1':formFile1,
        # 'formFile2':formFile2,'formFile3':formFile3,
        'form1':form1,'form2':form2,'utilisateur':utilisateur})

@login_required
def DisplayEvents(request):
    ok=''
    utilisateur = request.user
    ageUtilisateur = from_dob_to_age(utilisateur.birth)

    if request.method == 'POST' and utilisateur.is_authenticated:
        if(request.POST.get('formDemandeParticipation') != None and int(request.POST.get('formDemandeParticipation'))):
            Event.objects.get(id=request.POST.get('event_id')).attenteWinker.add(utilisateur)

            data = {}
            data['value'] = 1
            
            return JsonResponse(data)

        if 'SignalerArticle' in request.POST:
            # try:
            #     SignalerArticle.objects.filter(winkerSignalement=utilisateur).filter(eventSignalement= Event.objects.get(id=int(request.POST.get('SignalerArticle')))).delete()
            #     SignalerArticle.objects.create(raisonSignalement=request.POST.get('raisonSignalement'), winkerSignalement=utilisateur,eventSignalement= Event.objects.get(id=int(request.POST.get('identificationEvent'))))
            # except:
            SignalerArticle.objects.create(raisonSignalement=request.POST.get('raisonSignalement'), winkerSignalement=utilisateur,eventSignalement= Event.objects.get(id=int(request.POST.get('identificationEvent'))))

        
        if(request.POST.get('formAddLike') != None and int(request.POST.get('formAddLike'))):
            try:
                ReactionEvent.objects.filter(winkerReaction=utilisateur).filter(eventReaction=Event.objects.get(id=request.POST.get('event_id'))).delete()
                ReactionEvent.objects.create(reaction=1,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=request.POST.get('event_id')))
            except:
                ReactionEvent.objects.create(reaction=1,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=request.POST.get('event_id')))
      

            objEvent = Event.objects.get(id=request.POST.get('event_id'))
            objEvent.nbLike = ReactionEvent.objects.filter(eventReaction=objEvent).filter(reaction=1).count()
            objEvent.save()

            data = {}
            data['value'] = objEvent.nbLike


            return JsonResponse(data)

        if(request.POST.get('formAddLove') != None and int(request.POST.get('formAddLove'))):

            try:
                ReactionEvent.objects.filter(winkerReaction=utilisateur).filter(eventReaction=Event.objects.get(id=request.POST.get('event_id'))).delete()
                ReactionEvent.objects.create(reaction=5,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=request.POST.get('event_id')))
            except:
                ReactionEvent.objects.create(reaction=5,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=request.POST.get('event_id')))
      
            objEvent = Event.objects.get(id=request.POST.get('event_id'))
            objEvent.nbLove = ReactionEvent.objects.filter(eventReaction=Event.objects.get(id=request.POST.get('event_id'))).filter(reaction=5).count()
            objEvent.save()

            data = {}
            data['value'] = objEvent.nbLove

            return JsonResponse(data)


        if(request.POST.get('formAddSad') != None and int(request.POST.get('formAddSad'))):

            try:
                ReactionEvent.objects.filter(winkerReaction=utilisateur).filter(eventReaction=Event.objects.get(id=request.POST.get('event_id'))).delete()
                ReactionEvent.objects.create(reaction=4,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=request.POST.get('event_id')))
            except:
                ReactionEvent.objects.create(reaction=4,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=request.POST.get('event_id')))
            
            objEvent = Event.objects.get(id=request.POST.get('event_id'))
            objEvent.nbSad = ReactionEvent.objects.filter(eventReaction=Event.objects.get(id=request.POST.get('event_id'))).filter(reaction=4).count()
            objEvent.save()

            data = {}
            data['value'] = objEvent.nbSad

            return JsonResponse(data)

        if(request.POST.get('formAddWow') != None and int(request.POST.get('formAddWow'))):

            try:
                ReactionEvent.objects.filter(winkerReaction=utilisateur).filter(eventReaction=Event.objects.get(id=request.POST.get('event_id'))).delete()
                ReactionEvent.objects.create(reaction=3,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=request.POST.get('event_id')))
            except:
                ReactionEvent.objects.create(reaction=3,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=request.POST.get('event_id')))
      
            objEvent = Event.objects.get(id=request.POST.get('event_id'))
            objEvent.nbWow = ReactionEvent.objects.filter(eventReaction=Event.objects.get(id=request.POST.get('event_id'))).filter(reaction=3).count()
            objEvent.save()

            data = {}
            data['value'] = objEvent.nbWow

            return JsonResponse(data)

        if(request.POST.get('formAddAngry') != None and int(request.POST.get('formAddAngry'))):

            try:
                ReactionEvent.objects.filter(winkerReaction=utilisateur).filter(eventReaction=Event.objects.get(id=request.POST.get('event_id'))).delete()
                ReactionEvent.objects.create(reaction=-1,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=request.POST.get('event_id')))
            except:
                ReactionEvent.objects.create(reaction=-1,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=request.POST.get('event_id')))
      
            objEvent = Event.objects.get(id=request.POST.get('event_id'))
            objEvent.nbAngry = ReactionEvent.objects.filter(eventReaction=Event.objects.get(id=request.POST.get('event_id'))).filter(reaction=-1).count()
            objEvent.save()

            data = {}
            data['value'] = ReactionEvent.objects.filter(eventReaction=Event.objects.get(id=request.POST.get('event_id'))).filter(reaction=-1).count()

            return JsonResponse(data)

        if(request.POST.get('formAddHaha') != None and int(request.POST.get('formAddHaha'))):

            try:
                ReactionEvent.objects.filter(winkerReaction=utilisateur).filter(eventReaction=Event.objects.get(id=request.POST.get('event_id'))).delete()
                ReactionEvent.objects.create(reaction=2,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=request.POST.get('event_id')))
            except:
                ReactionEvent.objects.create(reaction=2,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=request.POST.get('event_id')))
      
            objEvent = Event.objects.get(id=request.POST.get('event_id'))
            objEvent.nbHaha = ReactionEvent.objects.filter(eventReaction=Event.objects.get(id=request.POST.get('event_id'))).filter(reaction=2).count()
            objEvent.save()

            data = {}
            data['value'] = objEvent.nbHaha

            return JsonResponse(data)

        if 'removeLike' in request.POST:
            ReactionEvent.objects.filter(winkerReaction=utilisateur).filter(eventReaction=Event.objects.get(id=int(request.POST.get('removeLike')))).delete()

        if 'addDislike' in request.POST:
            try:
                ReactionEvent.objects.filter(winkerReaction=utilisateur).filter(eventReaction=Event.objects.get(id=int(request.POST.get('addDislike')))).delete()
                ReactionEvent.objects.create(reaction=-1,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=int(request.POST.get('addDislike'))))
            except:
                ReactionEvent.objects.create(reaction=-1,winkerReaction=utilisateur,eventReaction=Event.objects.get(id=int(request.POST.get('addDislike'))))
        if 'removeDislike' in request.POST:
            ReactionEvent.objects.filter(winkerReaction=utilisateur).filter(eventReaction=Event.objects.get(id=int(request.POST.get('removeDislike')))).delete()


        


    ListIdEventParticipe = [x.id for x in Event.objects.filter(creatorWinker=utilisateur.id)]
    for x in Event.objects.filter(participeWinker=utilisateur.id):
        ListIdEventParticipe.append(x.id)

    ListIdEventSignal = [x.eventSignalement.id for x in SignalerArticle.objects.filter(winkerSignalement=utilisateur) ]


    events = Event.objects.filter(ageMinimum__lte=ageUtilisateur).filter(ageMaximum__gte=ageUtilisateur).exclude(id__in=ListIdEventParticipe).exclude(id__in=ListIdEventSignal)[::-1]

    
    dataFilesEvents = {}
    dataReactionEvents = {} #en cle on a l'id de l'event et apres c'est une liste avec en index 0 la reaction de l'user et en index le nb de like de l'event
    for event in events:
        dataFilesEvents[event.id] = [x.image for x in FilesEvent.objects.filter(event = event)]
        try:
            dataReactionEvents[event.id] = ReactionEvent.objects.filter(eventReaction=event).filter(winkerReaction=utilisateur)[0].reaction
        except:
            dataReactionEvents[event.id] = 0
       

    
    

    return render(request,'DisplayEvents.html',{
        'ok':ok,
        'utilisateur':utilisateur,
        'numberFiles':[1,2,3],
        'events':events,
        'dataReactionEvents':dataReactionEvents,
        'dataFilesEvents':dataFilesEvents})

@login_required
def DemandeParticipation(request):
    #Il faut d'abord trouver l'id de tous les evenements crées par l'utilisateur ( sous forme de liste )


    #Il faut maintenant aller dans la table d'association attente et afficher l'id de tous les winkers qui etaient en attente


    #Si il accepte la demande, alors il faudra mettre le winker dans la relation de participation à l'évènement et supp l'attente de la base
    return render(request,'DemandeParticipation.html',{})

@login_required
def Attente(request):
    utilisateur = Winker.objects.get(id=request.user.id)
    L=[]
    MyEvents = [Event.objects.get(id=event.id) for event in Event.objects.filter(creatorWinker=utilisateur.id)]
    dataDemandeAttente = {}
    for idEvent in [event.id for event in MyEvents]:
        dataDemandeAttente[Event.objects.get(id=idEvent)] = list(Counter([Winker.objects.get(id=winker.id) for winker in Winker.objects.filter(attenteEvent=idEvent) if winker.id != utilisateur.id]))

    IdEventWait = [x.id for x in Event.objects.filter(attenteWinker=utilisateur.id)]
    EventWait = [Event.objects.get(id=x) for x in IdEventWait]
    if request.method == 'POST':
        if 'AccepteDemande' in request.POST:
            for idEvent,ListIdAttente in dataDemandeAttente.items():
                for idAttente in ListIdAttente:
                    if request.POST.get(str(idEvent.id)+ " " +str(idAttente.id)):
                        L = request.POST.get(str(idEvent.id) + " " + str(idAttente.id)).split()
                        Event.objects.get(id=int(L[0])).participeWinker.add(Winker.objects.get(id=int(L[1])))

                        Event.objects.get(id=int(L[0])).attenteWinker.remove(Winker.objects.get(id=int(L[1])))
        
        if 'AnnuleDemande' in request.POST:
            for event in EventWait:
                if(request.POST.get(str(event.id))):
                    Event.objects.get(id=int(event.id)).attenteWinker.remove(Winker.objects.get(id=utilisateur.id))
                        
                            

    return render(request,'Attente.html',{
        'utilisateur':utilisateur,'MyEvents':MyEvents,
        'dataDemandeAttente':dataDemandeAttente.items(),
        'EventWait':EventWait
    })

@login_required
def ParticipeEvent(request,idEvent):
    utilisateur = Winker.objects.get(id=request.user.id)
    MyEvent = Event.objects.get(id=idEvent)
    objRamener = RamenerEvent.objects.filter(event = idEvent)
    objParticipantEvent = []
    objParticipantEvent.append(Event.objects.get(id=idEvent).creatorWinker)
    for x in Winker.objects.filter(participeEvent=idEvent):
        objParticipantEvent.append(x)

    moyenneAge = mean([from_dob_to_age(x.birth) for x in objParticipantEvent ])
    nbFille = len([x for x in objParticipantEvent if x.sexe == 'Feminin'])
    nbGarcon = len([x for x in objParticipantEvent if x.sexe == 'Masculin'])

    MyEvent.moyenneAge = moyenneAge
    MyEvent.nbFille = nbFille
    MyEvent.nbGarcon = nbGarcon
    MyEvent.save()


    if request.method == 'POST':
        if 'nouvelleDemande' in request.POST:
            message = str(request.POST.get('message'))
            RamenerEvent.objects.create(message = message, event = Event.objects.get(id=idEvent))
        if 'ModifOK' in request.POST:
            RamenerObj = RamenerEvent.objects.get(id=int(request.POST.get('ObjID')))
            RamenerObj.fait = 1
            RamenerObj.save()
        if 'ModifAnnule' in request.POST:
            RamenerObj = RamenerEvent.objects.get(id=int(request.POST.get('ObjID')))
            RamenerObj.fait = 0
            RamenerObj.save()
        if 'quitterEvent' in request.POST:
            Event.objects.get(id=idEvent).participeWinker.remove(Winker.objects.get(id=utilisateur.id))
            return redirect('/profil/')


    return render(request,'ParticipeEvent.html',{
        'creatorWinker':Event.objects.get(id=idEvent).creatorWinker,
        'utilisateur':utilisateur,
        'objRamener':objRamener,
        'objParticipantEvent':objParticipantEvent,
        'MyEvent':MyEvent,
    })

@login_required
def VoirProfil(request, idWinker):

    utilisateur = Winker.objects.get(id=request.user.id)
    photoProfil = Winker.objects.get(id=idWinker).photoProfil
    filesWinker = [photoProfil.url]
    for x in FilesWinker.objects.filter(winker=idWinker):
        filesWinker.append(x.image.url)
    VoirWinker = Winker.objects.get(id=idWinker)
    return render(request,'VoirProfil.html',{
        'utilisateur':utilisateur,
        'numberFiles':range(1,len(filesWinker)+1),
        'filesWinker':zip(filesWinker,range(1,len(filesWinker)+1)),
    })

@login_required
def Chat(request,idUser):
    user = request.user
    other_user = Winker.objects.get(id=idUser)
    return render(request,'Chat.html',{'user':user,'other_user':other_user})