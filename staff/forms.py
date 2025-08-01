from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model
from .models import Teacher 

User = get_user_model()

class TeacherCreationForm(ModelForm):
    '''Form for creating a new teacher'''
    # first_name = forms.CharField(max_length=30)
    # last_name = forms.CharField(max_length=30)
    # email = forms.EmailField(required=True)
    # password = forms.CharField(widget=forms.PasswordInput)
    # #Id_no = forms.CharField(max_length=50)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email
        
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'phone', 'TSC', 'password']
        widgets = {
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
            'TSC':forms.NumberInput(attrs={'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['user'].required = False  # Make user field optional