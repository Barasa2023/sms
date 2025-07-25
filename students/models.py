from django.db import models

from sms.settings import AUTH_USER_MODEL

class Student(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    adm_no = models.CharField(max_length=100)
    grade = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"