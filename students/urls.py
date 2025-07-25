from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.StudentList.as_view(), name = 'student_list')
]