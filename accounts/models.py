from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''
    Manage User creation
    '''
    email = models.EmailField(unique=True)
    username = None
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__s(self):
        return self.email
