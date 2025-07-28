from django.db import models
from django.contrib.auth import get_user_model
from academics.models import ClassRoom
from finance.models import FeeType

#from sms.settings import USER_AUTH_MODEL

User = get_user_model()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adm_no = models.CharField(max_length=100)
    grade = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    fee_type = models.ManyToManyField('finance.FeeType', blank=True)

    def total_fees(self):
        """Calculate total fees for the student."""
        if not self.pk:
            return 0
        return sum(fee.amount for fee in self.fee_type.all())

    def total_fees_paid(self):
        """Calculate total fees paid by the student."""
        if not self.pk:
            return 0
        return sum(payment.amount for payment in self.payment_set.all())
    
    def balance(self):
        """Calculate the balance of fees for the student."""
        if not self.pk:
            return 0
        total_paid = self.total_fees_paid()
        total_fees = sum(fee.amount for fee in self.fee_type.all())
        return total_fees - total_paid

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"