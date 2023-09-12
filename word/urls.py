from django.urls import path
from .views import *

urlpatterns = [
    path('add/', AddWord.as_view()),
    path('modify/<int:id>', ModifyWord.as_view()),
    path('delete/<int:id>', DeleteWord.as_view()),
    path('info/<int:id>', GetWord.as_view()),
    path('<int:page>', GetWords.as_view()),
]
