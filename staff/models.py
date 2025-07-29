from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Teacher(models.Model):
    '''Teacher management'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    Id_no = models.CharField(max_length=50)
    hire_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
