from django.urls import path
from .views import *

urlpatterns = [
    path('add/', AddStudy.as_view()),
    path('delete/<int:id>', DeleteStudy.as_view()),
    path('<int:page>', GetStudies.as_view()),
    path('all', GetAllStudies.as_view()),
]
