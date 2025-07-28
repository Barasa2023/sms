from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Admin interface for Student model."""
    # Display fields in the admin list view
    first_name = 'user__first_name'
    last_name = 'user__last_name'
    list_display = ['adm_no', 'grade', first_name, last_name, 'total_fees', 'balance']