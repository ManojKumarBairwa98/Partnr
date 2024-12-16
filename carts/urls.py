from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', include('users.urls') ),
    path('register/', include('users.urls') )
]