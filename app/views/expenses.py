from django.shortcuts import render
from app.forms.expenses import ExpensesForm
from django.shortcuts import redirect


# Create your view here.


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


def edit_expense(request):
    return render(request, 'expense-edit.html')


def delete_expense(request):
    return render(request, 'expense-delete.html')
