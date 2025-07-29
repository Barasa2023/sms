from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth import get_user_model
from django.db.models import Sum, Q
from .models import Student
from .forms import StudentCreationForm, StudentEditForm
from finance.models import Payment
from academics.models import ClassRoom

User = get_user_model()

# Create your views here.

def indexview(request):
    total_students = Student.objects.count()
    total_fee_collected = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
    total_fee_pending = sum([s.balance() for s in Student.objects.all()])
    total_classes = ClassRoom.objects.count()

    context = {
        'total_students': total_students,
        'total_fee_collected': total_fee_collected,
        'total_fee_pending': total_fee_pending,
        'total_classes': total_classes
    }
    return render(request, 'students/index.html', context)

class StudentList(ListView):
    '''List all students'''
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset =  Student.objects.select_related('user').all()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(adm_no__icontains=query) 
            )
        return queryset

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

class StudentDetail(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'