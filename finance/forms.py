from django import forms
from django.forms import ModelForm
from finance.models import FeeType, Fee
from students.models import Student, Payment

class FeeTypeForm(ModelForm):
    class Meta:
        model = FeeType
        fields = ['name', 'description', 'amount']


class FeePaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'fee', 'amount', 'payment_date', 'payment_method', 'receipt_number']
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }