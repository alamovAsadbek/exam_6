from django.urls import path

from likes.views import like_post
from users.views import login_view, logoutView, register_view, verify_email, profileView, error404View
from .views import *

urlpatterns = [
    path('', landingPageView, name='home'),
    path('auth/login', login_view, name='login'),
    path('auth/logout', logoutView, name='logout'),
    path('auth/register', register_view, name='register'),
    path('feedbacks', feedbacksView, name='feedbacks'),
    path('feedbacks/create', offerFormView, name='create_feedback'),
    path('feedbacks/<int:pk>/', feedbackDetailView, name='feedback_detail'),
    path('comments/', commentsView, name='create_comment'),
    path('profile', profileView, name='profile'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify_email'),
    path('404', error404View, name='error404'),
    path('like-post/', like_post, name='like_post'),
]
