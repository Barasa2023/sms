from django.db import models
from staff.models import Teacher

# Create your models here.
class ClassRoom(models.Model):
    '''Manage Classes'''
    streams = [
        ('N', 'North'),
        ('S', 'South'),
        ('E', 'East')
    ]
    capacity = models.IntegerField()
    class_teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    stream = models.CharField(max_length=50, choices=streams, default='N')
    name = models.CharField(max_length=50)


    def total_students(self):
        """Calculate total students in the classroom."""
        return self.student_set.count()
    
    def total_fees_collected(self):
        """Calculate total fees collected in the classroom."""
        return sum(student.total_fees_paid() for student in self.student_set.all())
    
    def fees_pending(self):
        """Calculate total fees pending in the classroom."""
        return sum(student.balance() for student in self.student_set.all())

    def __str__(self):
        return self.name

class Subject(models.Model):
    '''Manage Subjects'''
    grade = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_name