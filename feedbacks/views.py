from django.shortcuts import render


def feedbacksView(request):
    return render(request, 'offers/offer.html')


# Home page view
def landingPageView(request):
    return render(request, 'index/index.html')
