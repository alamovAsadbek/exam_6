from django.urls import path

from .views import *

urlpatterns = [
    path('', landingPageView, name='home'),
    path('auth/login', login_view, name='login'),
    path('auth/logout', logoutView, name='logout'),
    path('auth/register', registerView, name='register'),
    path('feedbacks', feedbacksView, name='feedbacks'),
    path('feedbacks/create', offerFormView, name='create_feedback'),
    path('comments/', commentsView, name='create_comment'),
    path('profile', profileView, name='profile'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify_email')
]
