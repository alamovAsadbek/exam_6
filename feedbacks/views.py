from django.contrib.auth import logout
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import UserModel
from users.token import email_token_generator


def feedbacksView(request):
    return render(request, 'offers/offer.html')


# Home page view
def landingPageView(request):
    return render(request, 'index/index.html')


def commentsView(request):
    return render(request, 'comments/comment.html')


def offerFormView(request):
    return render(request, 'forms/offer/offer-form.html')


def loginView(request):
    return render(request, 'auth/login/login.html')


def logoutView(request):
    logout(request)
    return render(request, 'index/index.html')


def registerView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'auth/register/register.html')


def profileView(request):
    return render(request, 'profile/profile.html')


def verifyEmailView(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(force_bytes(uidb64)))
        user = UserModel.objects.get(pk=uid)
        if email_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, 'components/success/success_page.html')
        else:
            return redirect(reverse_lazy('login'))
    except Exception as e:
        print(f'Error: {e}')
        return redirect(reverse_lazy('login'))


def send_email_verification(request, user):
    token = email_token_generator.make_token(request.user)
    uid = urlsafe_base64_encode(force_bytes(request.user.pk))
    domain = request.get_host()
    verification_url = reverse('verify-email', kwargs={'uidb64': uid, 'token': token})
    full_url = f'https://{domain}{verification_url}'

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
