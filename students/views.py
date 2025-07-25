from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth import get_user_model
from .models import Student

# Create your views here.
class StudentList(ListView):
    '''List all students'''
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.select_related('user').all()
