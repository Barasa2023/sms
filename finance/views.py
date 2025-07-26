from django.shortcuts import render
from django.views.generic import ListView, CreateView

from finance.models import Fee
from finance.models import Fee, FeeType
from finance.forms import FeeTypeForm

# Create your views here.
class FeeListView(ListView):
    '''List all fees'''
    model = Fee
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
        fee_type = form.cleaned_data['name']
        description = form.cleaned_data['description']
        amount = form.cleaned_data['amount']

        fee = FeeType.objects.create(
            name=fee_type,
            description=description,
            amount=amount
        )
        return super().form_valid(form)