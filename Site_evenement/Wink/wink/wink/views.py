from django.shortcuts import render
from profil.models import Winker

# Create your views here.
def murPrincipal(request):
    utilisateur = Winker.objects.get(id=request.user.id)
    return render(request,'murPrincipale.html',{'utilisateur':utilisateur})

