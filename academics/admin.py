from django.contrib import admin
from .models import ClassRoom, Subject

# Register your models here.
@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'capacity']