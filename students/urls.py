from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.StudentList.as_view(), name = 'student_list'),
    path('add/', views.StudentCreate.as_view(), name = 'add_student'),
    path('edit/<int:pk>/', views.StudentUpdate.as_view(), name = 'edit_student'),
]