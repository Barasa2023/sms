from django import forms
from .models import ClassRoom, Subject

class ClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ['name', 'class_teacher', 'capacity', 'stream']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_teacher': forms.Select(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'stream': forms.Select(attrs={'class': 'form-control'}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['sub_name', 'teacher', 'grade']
        widgets = {
            'sub_name': forms.TextInput(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'grade': forms.Select(attrs={'class': 'form-control'}),
        }

class ClassCreationForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ['name', 'class_teacher', 'capacity', 'stream']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_teacher': forms.Select(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'stream': forms.Select(attrs={'class': 'form-control'}),
        }