from django.shortcuts import render
from app.models import *

def profile_index(request):

    return render(request, 'profile.html')

def profile_edit(request):

    return render(request, 'profile-edit.html')

def profile_delete(request):

    return render(request, 'profile-delete.html')