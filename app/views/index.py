from django.shortcuts import render, redirect
from app.models import Profile, Expense
from app.forms.profiles import *
from app.common.budget import calculate_budget_left


# Create your view here.


def index(request):
    if Profile.objects.exists():
        profile = Profile.objects.all()[0]
        expenses = Expense.objects.all()
        expenses_cost =calculate_budget_left(profile,expenses)
        context = {
            'left': expenses_cost,
            'expenses': expenses,
            'form': ProfileForm(),
            'profile': profile,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        context = {
            'form': ProfileForm(),
        }
        return render(request, 'home-no-profile.html', context)
