from django.shortcuts import render
from app.models import Profile,Expense
from app.forms.profiles import *
# Create your views here.


def index(request):
    
    
   
    if Profile.objects.exists():
        profile=Profile.objects.all()[0]
        expenses=Expense.objects.all()
        context={
            'expenses':expenses,
            'form':ProfileForm(),
            'profile':profile,
        }
        return render(request, 'home-with-profile.html',context)
    else:
        return render(request, 'home-no-profile.html')