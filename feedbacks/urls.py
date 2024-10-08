from django.conf.urls.i18n import i18n_patterns
from django.urls import path

from .views import *

urlpatterns = i18n_patterns(
    path('', landingPageView, name='home'),
    path('auth/login', loginView, name='login'),
    path('auth/logout', logoutView, name='logout'),
    path('auth/register', registerView, name='register'),
    path('feedbacks', feedbacksView, name='feedbacks'),
    path('feedbacks/create', offerFormView, name='create_feedback'),
    path('comments/<int:feedback_id>', commentsView, name='create_comment'),
    path('profile', profileView, name='profile')
)
