from django.urls import path

from comments.views import createCommentView
from users.views import login_view, logoutView, register_view, profileView, error404View, verify_email
from .views import *

urlpatterns = [
    path('', landingPageView, name='home'),
    path('auth/login', login_view, name='login'),
    path('auth/logout', logoutView, name='logout'),
    path('auth/register', register_view, name='register'),
    path('feedbacks', feedbacksView, name='feedbacks'),
    path('feedbacks/create', offerFormView, name='create_feedback'),
    path('feedbacks/<int:pk>/', createCommentView, name='feedback_detail'),
    path('comments/', commentsView, name='create_comment'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify-email'),
    path('profile', profileView, name='profile'),
    path('404', error404View, name='error404'),
]
