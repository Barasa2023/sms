from django.urls import path
from . import views

app_name = 'academics'

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('classrooms/', views.ClassRoomListView.as_view(), name='classroom_list'),
    path('classrooms/add/', views.ClassRoomCreateView.as_view(), name='add_classroom'),
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/add/', views.SubjectCreateView.as_view(), name='add_subject'),
]