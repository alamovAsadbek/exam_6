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
from feedbacks.forms import FeedbackMainForm
from frequently_questions.models import FrequentlyQuestionsModel
from team_users.models import TeamUserModel
from users.forms import UserLoginForm, UserRegisterForm
from users.models import UserModel
from users.token import email_token_generator


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
        print(request.POST)
        form = FeedbackMainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
        else:
            errors = form.errors
            return render(request, 'forms/offer/offer-form.html', {'errors': errors})
    else:
        return render(request, 'forms/offer/offer-form.html')


def logoutView(request):
    logout(request)
    return render(request, 'index/index.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            send_email_verification(request, user)
            return redirect(reverse_lazy('login'))
        else:
            errors = form.errors
            return render(request, 'auth/register/register.html', {'errors': errors})
    else:
        return render(request, 'auth/register/register.html')


def profileView(request):
    return render(request, 'profile/profile.html')


def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(pk=uid)
        if email_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            return redirect(reverse_lazy('login'))
    except Exception as e:
        print(f'Error: {e}')
        return redirect(reverse_lazy('login'))


def send_email_verification(request, user):
    token = email_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    domain = request.get_host()
    verification_url = reverse('verify_email', kwargs={'uidb64': uid, 'token': token})
    full_url = f'http://{domain}{verification_url}'

    text_content = render_to_string(
        'components/verify_email/verify_email.html',
        {'user': user, 'full_url': full_url}
    )

    message = EmailMultiAlternatives(
        subject='Verify your email',
        body=text_content,
        from_email=EMAIL_HOST_USER,
        to=[user.email]
    )

    message.attach_alternative(text_content, "text/html")
    message.send()


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']

            # Check if input is an email
            try:
                validate_email(username_or_email)
                is_email = True
            except ValidationError:
                is_email = False

            if is_email:
                user_data = UserModel.objects.filter(email=username_or_email.lower()).first()
                if user_data and user_data.is_active:
                    username = user_data.username
                else:
                    username = None
            else:
                user_data = UserModel.objects.filter(username=username_or_email.lower()).first()
                if user_data and user_data.is_active:
                    username = username_or_email
                else:
                    username = None

            if username:
                user = authenticate(request=request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect(reverse_lazy('home'))
                else:
                    return render(request, 'auth/login/login.html', {
                        'error': 'Invalid login details or account not activated. Please check your email.'
                    })
            else:
                return render(request, 'auth/login/login.html', {'error': 'Invalid login details.'})
    else:
        return render(request, 'auth/login/login.html')
