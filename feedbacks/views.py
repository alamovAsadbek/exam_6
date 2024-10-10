from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from config.settings import EMAIL_HOST_USER
from frequently_questions.models import FrequentlyQuestionsModel
from team_users.models import TeamUserModel
from users.forms import UserLoginForm, UserRegisterForm
from users.models import UserModel
from users.token import email_token_generator
from .forms import FeedbackOfferForm, FeedbackProblemForm


def feedbacksView(request):
    return render(request, 'offers/offer.html')


# Home page view
def landingPageView(request):
    all_frequently_asked_questions = FrequentlyQuestionsModel.objects.all()
    team_members = TeamUserModel.objects.all()
    context = {
        'all_frequently_asked_questions': all_frequently_asked_questions,
        'team_members': team_members
    }
    return render(request, 'index/index.html', context)


def commentsView(request):
    return render(request, 'comments/comment.html')


def offerFormView(request):
    if request.method == 'POST':
        keys = request.POST.keys()
        second_key = list(keys)[4]
        form = FeedbackOfferForm(request.POST)
        if second_key == 'problemForm':
            form = FeedbackProblemForm(request.POST)
        if form.is_valid():
            if second_key == 'problemForm':
                form.cleaned_data['feedback_type'] = 'problem'
            print(form.cleaned_data)
            form.save()
            return redirect(reverse_lazy('home'))
        else:
            errors = form.errors
            return render(request, 'offers/offer.html', {'errors': errors})
    else:
        return render(request, 'forms/offer/offer-form.html')


