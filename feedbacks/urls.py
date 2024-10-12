from django.urls import path

from comments.views import createCommentView, commentDetailView
from likes.views import LikeView, UnlikeView
from users.views import login_view, logoutView, register_view, verify_email, profileView, error404View
from .views import *

urlpatterns = [
    path('', landingPageView, name='home'),
    path('auth/login', login_view, name='login'),
    path('auth/logout', logoutView, name='logout'),
    path('auth/register', register_view, name='register'),
    path('feedbacks', feedbacksView, name='feedbacks'),
    path('feedbacks/create', offerFormView, name='create_feedback'),
    path('feedbacks/<int:pk>/', createCommentView, name='feedback_detail'),
    path('comments/<int:pk>/<int:user_id>/', commentDetailView, name='comment_detail'),
    path('comments/', commentsView, name='create_comment'),
    path('profile', profileView, name='profile'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify_email'),
    path('404', error404View, name='error404'),

    # for likes
    path('api/like/', LikeView.as_view(), name='like'),
    path('api/unlike/', UnlikeView.as_view(), name='unlike'),
]
