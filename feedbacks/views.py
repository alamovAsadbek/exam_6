from django.shortcuts import render


def feedbacksView(request):
    return render(request, 'offers/offer.html')
