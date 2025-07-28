from django import forms
from django.forms import ModelForm
from finance.models import FeeType
from . models import Student
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentCreationForm(ModelForm):
    '''Student creation form'''
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    fee_type = forms.ModelMultipleChoiceField(
        queryset = FeeType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Fee Categories"
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'adm_no', 'grade', 'fee_type']

class StudentEditForm(ModelForm):
    '''Student edit form'''
    #first_name = forms.CharField(max_length=50)
    #last_name = forms.CharField(max_length=50)
    #email = forms.EmailField(required=True)
    fee_type = forms.ModelMultipleChoiceField(
        queryset=FeeType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Fee Categories"
    )
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'adm_no', 'grade', 'fee_type']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'adm_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admission Number'}),
            'grade': forms.Select(attrs={'class': 'form-select'}),
            'fee_type': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }