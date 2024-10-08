from django.shortcuts import render


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


def registerView(request):
    return render(request, 'auth/register/register.html')


def profileView(request):
    return render(request, 'profile/profile.html')
