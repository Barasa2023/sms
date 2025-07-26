from django import forms
from django.forms import ModelForm
from finance.models import FeeType

class FeeTypeForm(ModelForm):
    class Meta:
        model = FeeType
        fields = ['name', 'description', 'amount']