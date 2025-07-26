from django.db import models
from django.contrib.auth import get_user_model
from academics.models import ClassRoom

#from sms.settings import USER_AUTH_MODEL

User = get_user_model()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adm_no = models.CharField(max_length=100)
    grade = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"