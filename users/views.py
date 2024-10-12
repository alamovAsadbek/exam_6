from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from users.forms import UserRegisterForm


def logoutView(request):
    logout(request)
    return render(request, 'index/index.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False  # Foydalanuvchini dastlab faollashtirmang
            user.save()
            send_email_verification(request, user)
            return redirect(reverse_lazy('login'))
        else:
            errors = form.errors
            return render(request, 'auth/register/register.html', {"errors": errors})
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register/register.html', {'form': form})


def login_view(request):
    return render(request, 'auth/login/login.html')


def profileView(request):
    pass


def error404View(request):
    return render(request, '404/404.html')
