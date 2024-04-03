from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('login/', views.patient_login, name='patient_login'),
    path('logout/', views.patient_logout, name='patient_logout'),
]
