from django.urls import path
from finance import views

app_name = 'finance'

urlpatterns = [
    path('', views.FeeListView.as_view(), name='fee_list'),
    path('add/', views.CreateFeeView.as_view(), name='add_fee'),
    path('payments/', views.FeePaymentListView.as_view(), name='fee_payments'),
    path('payments/add/', views.FeePaymentView.as_view(), name='add_payment'),
    path('payments/<int:pk>/edit/', views.FeeUpdateView.as_view(), name='fee_edit'),
    path('payments/<int:pk>/delete/', views.FeeDeleteView.as_view(), name='fee_delete'),
]
