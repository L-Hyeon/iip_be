from django.urls import path
from .views import *

urlpatterns = [
    path('changepw/', Changepw.as_view()),
    path('delete/<int:id>', DeleteUser.as_view()),
    path('info/<int:id>', GetUser.as_view()),
    path('<int:page>', GetUsers.as_view()),
]
