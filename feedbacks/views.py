from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from frequently_questions.models import FrequentlyQuestionsModel
from team_users.models import TeamUserModel
from .forms import FeedbackRequestForm
from .models import FeedbackModel


def feedbacksView(request):
    problems = FeedbackModel.objects.all().filter(feedback_type='problem')
    offers = FeedbackModel.objects.all().filter(feedback_type='offer').order_by('-created_at')
    context = {
        'problems': problems,
        'offers': offers,
    }
    return render(request, 'offers/offer.html', context)


# Home page view
def landingPageView(request):
    all_frequently_asked_questions = FrequentlyQuestionsModel.objects.all()
    team_members = TeamUserModel.objects.all()
    context = {
        'all_frequently_asked_questions': all_frequently_asked_questions,
        'team_members': team_members
    }
    return render(request, 'index/index.html', context)


def commentsView(request):
    return render(request, 'comments/comment.html')


def offerFormView(request):
    if request.method == 'POST':
        form = FeedbackRequestForm(request.POST)
        print(request.POST)
        if form.is_valid():
            keys = request.POST.keys()
            second_key = list(keys)[4]
            feedback = form.save(commit=False)
            if second_key == 'offerForm':
                feedback.user = request.user
            form.save()
            return redirect(reverse_lazy('feedbacks'))
        else:
            errors = form.errors
            return render(request, 'offers/offer.html', {'errors': errors})
    return render(request, 'forms/offer/offer-form.html')
