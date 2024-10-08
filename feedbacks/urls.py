from django.urls import path

from .views import *

urlpatterns = [
    path('auth/login', loginView, name='login'),
    path('auth/logout', logoutView, name='logout'),
]
