from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.indexview, name='index'),
    path('students/', views.StudentList.as_view(), name='student_list'),
    path('add/', views.StudentCreate.as_view(), name='add_student'),
    path('edit/<int:pk>/', views.StudentUpdate.as_view(), name='edit_student'),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name='student_detail')
]