from django.db import models
from staff.models import Teacher

# Create your models here.
class ClassRoom(models.Model):
    '''Manage Classes'''
    capacity = models.IntegerChoices(max = 60)
    class_teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    stream = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Subject(models.Model):
    '''Manage Subjects'''
    grade = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_name