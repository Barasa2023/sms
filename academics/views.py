from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import ClassRoomForm, SubjectForm
from .models import ClassRoom, Subject

class ClassRoomListView(ListView):
    '''List all classrooms'''
    model = ClassRoom
    template_name = 'academics/classroom_list.html'
    context_object_name = 'classrooms'

    def get_queryset(self):
        return ClassRoom.objects.all()
    
class ClassRoomCreateView(CreateView):
    model = ClassRoom
    form_class = ClassRoomForm
    template_name = 'academics/classroom_form.html'
    success_url = '/academics/classrooms/'  # Redirect to classroom list after creation

    def form_valid(self, form):
        name = form.cleaned_data['name']
        class_teacher = form.cleaned_data['class_teacher']
        capacity = form.cleaned_data['capacity']
        stream = form.cleaned_data['stream']

        # Create classroom instance
        classroom = form.save(commit=False)
        classroom.name = name
        classroom.class_teacher = class_teacher
        classroom.capacity = capacity
        classroom.stream = stream
        classroom.save()

        return super().form_valid(form)

class SubjectListView(ListView):
    '''List all subjects'''
    model = Subject
    template_name = 'academics/subject_list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        return Subject.objects.all()

class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'academics/subject_form.html'
    success_url = '/academics/subjects/'  # Redirect to subject list after creation

    def form_valid(self, form):
        sub_name = form.cleaned_data['sub_name']
        teacher = form.cleaned_data['teacher']
        grade = form.cleaned_data['grade']

        # Create subject instance
        subject = form.save(commit=False)
        subject.sub_name = sub_name
        subject.teacher = teacher
        subject.grade = grade
        subject.save()

        return super().form_valid(form)