from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from users.forms import UserRegisterForm
from users.models import UserModel
from users.token import email_token_generator


def logoutView(request):
    logout(request)
    return render(request, 'index/index.html')


# def verify_email(request, uidb64, token):
#     uid = force_str(urlsafe_base64_decode(uidb64))
#     user = UserModel.objects.get(pk=uid)
#     if user is not None and email_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         messages.success(request, 'Account activated')
#         return redirect(reverse_lazy('login'))
#     else:
#         messages.error(request, 'The verification link is invalid.')
#         return redirect(reverse_lazy('login'))
#
#
# def send_email_verification(request, user):
#     token = email_token_generator.make_token(user)
#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     current_site = get_current_site(request)
#     verification_url = reverse('verify_email', kwargs={'uidb64': uid, 'token': token})
#     full_url = f"http://{current_site.domain}/{verification_url}"
#
#     text_content = render_to_string(
#         'components/verify_email/verify_email.html',
#         {
#             'user': user,
#             'full_url': full_url,
#         }
#     )
#
#     message = EmailMultiAlternatives(
#         subject='Email Verification',
#         body=text_content,
#         to=[user.email],
#         from_email=settings.EMAIL_HOST_USER
#     )
#     message.attach_alternative(text_content, 'text/html')
#     message.send()
#
#
# def register_view(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.is_active = False
#             user.save()
#             send_email_verification(request, user)
#             return redirect(reverse_lazy('login'))
#         else:
#             errors = form.errors
#             return render(request, 'auth/register/register.html', {"errors": errors})
#     return render(request, template_name='auth/register/register.html')
#
#
# def login_view(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request=request, username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("/")
#             else:
#                 messages.error(request, 'Invalid username or password')
#                 return render(request, template_name='auth/login/login.html')
#     else:
#         return render(request, 'auth/login/login.html')
#
#
# def profileView(request):
#     return render(request, 'profile/profile.html')
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
            return render(request, 'auth/register/register.html', {"errors": errors})
    return render(request, template_name='auth/register/register.html')


def send_email_verification(request, user):
    token = email_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    verification_url = reverse('verify_email', kwargs={'uidb64': uid, 'token': token})
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


def verify_email(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = UserModel.objects.get(pk=uid)
    if user is not None and email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account activated')
        return redirect(reverse_lazy('login'))
    else:
        messages.error(request, 'The verification link is invalid.')
        return redirect(reverse_lazy('login'))


def login_view(request):
    pass


def profileView(request):
    pass
