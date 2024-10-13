from django.conf import settings
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from users.forms import RegisterForm, LoginForm, EditProfileForm
from users.models import ProfileModel
from users.token import email_token_generator


def logout_view(request):
    logout(request)
    return render(request, 'index/index.html')


def verify_email(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
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
    full_url = f"http://{current_site.domain}{verification_url}"

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
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            ProfileModel.objects.create(
                user_id=user.pk,
            )
            send_email_verification(request, user)
            return redirect('login')
        else:
            errors = form.errors
            return render(request, 'auth/register/register.html',
                          {"form": form, "errors": errors})
    else:
        form = RegisterForm()
    return render(request, 'auth/register/register.html', {"form": form})


def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('feedbacks')
            else:
                error_message = "Username yoki parol noto'g'ri"
        else:
            error_message = "Formada xato mavjud"
    print(error_message)
    return render(request, 'auth/login/login.html', {'error': error_message})


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    return render(request, 'profile/profile.html', {'user': user})


def update_profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            location = form.cleaned_data['location']
            organization = form.cleaned_data['organization_name']
            linkedin_url = form.cleaned_data['linkedin_url']
            if first_name is None:
                first_name = user.first_name
            if last_name is None:
                last_name = user.last_name
            if location is None:
                location = user.profile.location
            if organization is None:
                organization = user.profile.organization_name
            if linkedin_url is None:
                linkedin_url = user.profile.linkedin_url
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            user.profile.location = location
            user.profile.organization_name = organization
            user.profile.linkedin_url = linkedin_url
            user.profile.save()
            return redirect('profile')
        else:
            errors = form.errors
            return render(request, 'profile/profile.html',
                          {"form": form, "errors": errors})
    return render(request, 'profile/profile.html', {'user': user})


def error_404_view(request):
    return render(request, '404/404.html')
