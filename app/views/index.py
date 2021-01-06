from django.shortcuts import render,redirect
from app.models import Profile,Expense
from app.forms.profiles import *
# Create your views here.


def index(request):
    
    
   
    if Profile.objects.exists():
        profile=Profile.objects.all()[0]
        expenses=Expense.objects.all()
        budjet=Profile.objects.all()[0].budget
        left=float(budjet)
        for expense in expenses:
            left-= float(expense.price)
        context={
            'left':left,
            'expenses':expenses,
            'form':ProfileForm(),
            'profile':profile,
        }
        return render(request, 'home-with-profile.html',context)
    else:
        context={
            'form':ProfileForm(),
        }
        return render(request,'home-no-profile.html',context)