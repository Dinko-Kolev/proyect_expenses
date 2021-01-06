from django.shortcuts import render,redirect
from app.models import *
from django.views.decorators.http import require_POST
from app.forms.profiles import ProfileForm
from django.shortcuts import redirect

def profile_index(request):
    return render(request, 'profile.html')

@require_POST
def profile_create(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

def profile_edit(request):

    return render(request, 'profile-edit.html')

def profile_delete(request):

    return render(request, 'profile-delete.html')