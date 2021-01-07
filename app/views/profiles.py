from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from app.forms.profiles import ProfileForm, DeleteProfileForm
from django.shortcuts import redirect
from app.models import Profile, Expense
from app.common.budget import calculate_budget_left


def profile_index(request):
    profile = Profile.objects.all()[0]
    expenses = Expense.objects.all()
    expenses_cost = calculate_budget_left(profile, expenses)
    context = {
        'expenses': expenses_cost,
        'profile': profile,

    }
    return render(request, 'profile.html', context)


@require_POST
def profile_create(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        return render(request, 'home-no-profile.html')


def profile_edit(request):
    profile = Profile.objects.all()[0]
    if request.method == 'GET':
        context = {

            'form': ProfileForm(instance=profile),
        }
        return render(request, 'profile-edit.html', context)

    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile index')

        context = {

            'form': form,
        }
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        context = {
            'profile': profile,

            'form': DeleteProfileForm(instance=profile),
        }
        return render(request, 'profile-delete.html', context)

    else:
        profile.delete()
        [expense.delete() for expense in Expense.objects.all()]

        return redirect('index')
