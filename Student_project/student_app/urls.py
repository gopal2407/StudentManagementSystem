from django.urls import path
from .views import student_form, student_data, student_update, student_delete


urlpatterns = [
    path('student-form/', student_form, name='student_form_url'),
    path('student-data/', student_data, name='student_data_url'),
    path('student-update/<int:pk>/', student_update, name='student_update_url'),
    path('student-delete/<int:pk>/', student_delete, name='student_delete_url'),
]