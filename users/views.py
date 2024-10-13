from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from users.forms import UserRegisterForm, UserLoginForm
from users.models import UserModel
from users.token import email_token_generator


def logoutView(request):
    logout(request)
    return render(request, 'index/index.html')


def verify_email(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = UserModel.objects.get(pk=uid)
    if user is not None and email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect(reverse_lazy('login'))
    else:
        return redirect(reverse_lazy('login'))


def send_email_verification(request, user):
    token = email_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    verification_url = reverse('verify-email', kwargs={'uidb64': uid, 'token': token})
    full_url = f"http://{current_site.domain}/{verification_url}"

    text_content = render_to_string(
        'components/verify_email/verify_email.html',
        {
            'user': user,
            'full_url': full_url,
        }
    )

    message = EmailMultiAlternatives(
        subject='Email Verification',
        body=text_content,
        to=[user.email],
        from_email=settings.EMAIL_HOST_USER
    )
    message.attach_alternative(text_content, 'text/html')
    message.send()


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect('login')
        else:
            errors = form.errors
            return render(request, 'auth/register/register.html',
                          {"form": form, "errors": errors})
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register/register.html', {"form": form})


def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = UserModel.objects.filter(username=username, password=password).first()
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Username yoki parol noto'g'ri"
        else:
            error_message = "Formada xato mavjud"
    else:
        form = UserLoginForm()

    return render(request, 'auth/login/login.html', {'form': form, 'error': error_message})


def profileView(request):
    pass


def error404View(request):
    return render(request, '404/404.html')
