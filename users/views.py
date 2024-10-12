from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from users.forms import UserRegisterForm, UserLoginForm
from users.models import UserModel


def logoutView(request):
    logout(request)
    return render(request, 'index/index.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse_lazy('login'))
        else:
            errors = form.errors
            return render(request, 'auth/register/register.html', {"errors": errors})
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = UserModel.objects.filter(email=email).first()
            print(user)
            if user is not None:
                login(request, user)
                return redirect('feedbacks')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login/login.html', {'form': form})


def profileView(request):
    pass


def error404View(request):
    return render(request, '404/404.html')
