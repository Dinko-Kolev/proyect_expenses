from django.shortcuts import render
from app.forms.expenses import ExpensesForm
from django.shortcuts import redirect

# Create your view here.
from app.models import Expense


def create_expense(request):
    if request.method == 'GET':
        context = {
            'form': ExpensesForm(),
        }
        return render(request, 'expense-create.html', context)
    else:
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
        }
        return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': ExpensesForm(instance=expense),
        }
        return render(request, 'expense-edit.html', context)

    else:
        form = ExpensesForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'expense': expense,
            'form': form,
        }
        return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': ExpensesForm(instance=expense),
        }
        return render(request, 'expense-delete.html', context)

    else:
        form = ExpensesForm(request.POST, instance=expense)
        if form.is_valid():
            expense.delete()
            return redirect('index')

        context = {
            'expense': expense,
            'form': form,
        }
        return render(request, 'expense-delete.html', context)
