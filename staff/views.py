from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .models import Teacher
from .forms import TeacherCreationForm

User = get_user_model()

# Create your views here.
class IndexView(ListView):
    '''Return a list of all teachers'''
    model = Teacher
    template_name = 'staff/teacher_list.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        return Teacher.objects.select_related('user').all()

class CreateTeacherView(CreateView):
    model = Teacher
    form_class = TeacherCreationForm
    success_url = reverse_lazy('staff:index')

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        #Id_no = form.cleaned_data['id_no']
        password = form.cleaned_data['password']

        #create user
        user = User.objects.create_user(
            username=email,
            first_name=first_name,
            email=email,
            last_name=last_name,
            password=password
        )
        user.Id_no = form.cleaned_data.get('id_no', '')
        user.is_teacher=True
        user.save()

        teacher = form.save(commit=False)
        teacher.user = user
        teacher.save()


        return super().form_valid(form)
    