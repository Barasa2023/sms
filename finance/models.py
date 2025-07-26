from django.db import models
from students.models import Student

class FeeType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_type = models.ForeignKey(FeeType, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fee_type

class Payment(models.Model):
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    receipt_number = models.CharField(max_length=100, unique=True)

    def get_balance(self):
        total_paid = sum(payment.amount for payment in self.fee.payment_set.all())
        return self.fee.amount - total_paid

    def __str__(self):
        return f"Payment of {self.amount} for {self.fee.student.user.first_name} on {self.payment_date}"


