from django.shortcuts import render
from app.models import *
# Create your views here.



  
def create_expense(request):

    return render(request, 'expense-create.html')
    
def edit_expense(request):

    return render(request, 'expenses-edit.html')
  
def delete_expense(request):

    return render(request, 'expenses-delete.html')
