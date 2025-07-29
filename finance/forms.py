from django import forms
from django.forms import ModelForm
from finance.models import FeeType
from students.models import Student
from finance.models import Payment

class FeeTypeForm(ModelForm):
    class Meta:
        model = FeeType
        fields = ['name', 'description', 'amount']


class FeePaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'amount', 'fee', 'payment_method', 'receipt_number']
        widgets = {
            'student': forms.Select(attrs = {'class': 'form-control', 'placeholder': 'Select Student'}),
            'amount': forms.NumberInput(attrs = {'class': 'form-control', 'placeholder': 'Amount Paid'}),
            'fee': forms.Select(attrs = {'class': 'form-control', 'placeholder': 'Fee Category'}),
            'payment_method': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Payment Method'}),
            'receipt_number': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Receipt Number'})
        }

class FeeUpdateForm(ModelForm):
    class Meta:
        model = FeeType
        fields = ['name', 'description', 'amount']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fee Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }

class CreateFeeForm(ModelForm):
    class Meta:
        model = FeeType
        fields = ['name', 'description', 'amount']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fee Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }