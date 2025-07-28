from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from finance.models import Payment, FeeType
from students.models import Student
from .forms import FeePaymentForm

#from finance.models import Fee
from finance.models import FeeType
from finance.forms import FeeTypeForm

# Create your views here.
class FeeListView(ListView):
    '''List all fees'''
    model = FeeType
    template_name = 'finance/fee_list.html'
    context_object_name = 'fees'

    def get_queryset(self):
        return FeeType.objects.all()

class CreateFeeView(CreateView):
    '''Create a new fee'''
    model = FeeType
    form_class = FeeTypeForm
    template_name = 'finance/add_fee.html'
    success_url = '/finance/'  # Redirect to fee list after creation

    def form_valid(self, form):
        # fee_type = form.cleaned_data['name']
        # description = form.cleaned_data['description']
        # amount = form.cleaned_data['amount']

        # fee = FeeType.objects.create(
        #     name=fee_type,
        #     description=description,
        #     amount=amount
        # )
        return super().form_valid(form)
class FeePaymentView(CreateView):
    '''Create a new fee payment'''
    model = Payment
    form_class = FeePaymentForm
    template_name = 'finance/add_payment.html'
    success_url = '/finance/payments/'  # Redirect to payment list after creation

    def form_valid(self, form):
        # student = form.cleaned_data['student']
        # amount = form.cleaned_data['amount']
        # payment_method = form.cleaned_data['payment_method']
        # receipt_number = form.cleaned_data['receipt_number']

        # payment = Payment.objects.create(
        #     student=student,
        #     amount=amount,
        #     payment_method=payment_method,
        #     receipt_number=receipt_number
        # )
        return super().form_valid(form)
    
class FeePaymentListView(ListView):
    '''List all fee payments'''
    model = Payment
    template_name = 'finance/fee_payment_list.html'
    context_object_name = 'payments'

    def get_queryset(self):
        return Payment.objects.select_related('student').all()

class FeeUpdateView(UpdateView):
    '''Update an existing fee category'''
    model = FeeType
    form_class = FeeTypeForm
    template_name = 'finance/edit_fee.html'
    success_url = '/payments/'

    def get_object(self, queryset=None):
        return Payment.objects.get(pk=self.kwargs['pk'])
    
class FeeDeleteView(DeleteView):
    '''Delete an existing fee category'''
    model = FeeType
    template_name = 'finance/delete_fee.html'
    success_url = '/payments/'

    def get_object(self, queryset=None):
        return FeeType.objects.get(pk=self.kwargs['pk'])