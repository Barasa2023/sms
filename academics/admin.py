from django.contrib import admin
from .models import ClassRoom, Subject

# Register your models here.
@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'capacity']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['sub_name', 'teacher', 'grade']