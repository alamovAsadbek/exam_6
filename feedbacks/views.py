from django.contrib.auth import logout
from django.shortcuts import render, redirect

from users.forms import UserRegisterForm


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


def verifyEmailView(request):
    return render(request, 'profile/profile.html')
