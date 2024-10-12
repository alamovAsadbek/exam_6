from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from users.forms import UserRegisterForm, UserLoginForm


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
            user = authenticate(request=request, email=email, password=password)
            if user is not None:
                login(request, user)
                print(request.user)
                return redirect("feedbacks")
            else:
                return render(request, template_name='auth/login/login.html')
    else:
        return render(request, 'auth/login/login.html')


def profileView(request):
    pass


def error404View(request):
    return render(request, '404/404.html')
