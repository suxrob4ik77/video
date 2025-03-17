from django.urls import path
from .views import *

urlpatterns = [
    path('', loginPage, name='login'),  # Bosh sahifa login sahifasi bo‘lib turibdi
    path('index/', index, name='index'),

    path('student/<int:student_id>/', student, name='student_detail'),
    path('student/<int:student_id>/delete/', delete_student, name='delete_student'),  # URL to‘g‘rilandi
    path('student/<int:student_id>/pdf/', generate_student_pdf, name='generate_student_pdf'),

    path('fanlar/<int:fanlar_id>/', fanlar, name='fanlar_detail'),

    path('add/', add, name='add'),
]
