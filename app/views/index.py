from django.shortcuts import render
from app.models import *
# Create your views here.


def index(request):
    profiles= Profile.objects.all()
    profiles_count= profiles.count()
    if profiles_count >0:
        return render(request, 'home-with-profile.html')
    elif profiles_count==0:
        return render(request, 'home-no-profile.html')
    else:
        print('ERROR!!!')