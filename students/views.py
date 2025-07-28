from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth import get_user_model
from .models import Student
from .forms import StudentCreationForm

User = get_user_model()

# Create your views here.
class StudentList(ListView):
    '''List all students'''
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.select_related('user').all()

class StudentCreate(CreateView):
    model = Student
    form_class = StudentCreationForm
    template_name = 'students/student_add.html'
    success_url = '/students/'  # Redirect to student list after creation

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        username = email  # Use email as username
        #password = form.cleaned_data['password']

        #create user
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            email=email,
            last_name=last_name,
            #password=password
        )

        # Create student profile
        user.adm_no = form.cleaned_data['adm_no']
        user.is_student = True
        user.save()

        student = form.save(commit=False)
        student.user = user
        student.save()

        return super().form_valid(form)

class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentEditForm
    pk_url_kwarg = 'pk'
    template_name = 'students/student_edit.html'
    success_url = '/students/'
