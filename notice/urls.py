from django.urls import path
from .views import *

urlpatterns = [
    path('add/', AddNotice.as_view()),
    path('modify/<int:id>', ModifyNotice.as_view()),
    path('delete/<int:id>', DeleteNotice.as_view()),
    path('info/<int:id>', GetNotice.as_view()),
    path('<int:page>', GetNotices.as_view()),
]
