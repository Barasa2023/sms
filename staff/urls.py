from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    #path('list_teacher', views.ListTeacherView.as_view(), name = 'teacher_list'),
    path('teacher/', views.CreateTeacherView.as_view(), name = 'create_teacher')
]