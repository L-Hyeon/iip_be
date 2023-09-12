from django.contrib import admin
from django.urls import path, include

from user.views import *
from word.views import *
from study.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('logout', Logout.as_view()),
    path('user/', include('user.urls')),
    path('word/', include('word.urls')),
    path('study/', include('study.urls')),
    path('notice/', include('notice.urls')),
]
