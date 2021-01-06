from django import forms
from app.models import Expense


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
