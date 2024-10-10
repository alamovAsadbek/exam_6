from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from users.forms import UserRegisterForm
from users.models import UserModel


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
            return redirect(reverse_lazy('login'))
        else:
            return redirect(reverse_lazy('login'))
    except Exception as e:
        print(f'Error: {e}')
        return redirect(reverse_lazy('login'))
