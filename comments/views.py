from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from comments.models import CommentModel
from feedbacks.models import FeedbackModel


@login_required
def createCommentView(request, pk):
    try:
        feedback = FeedbackModel.objects.get(pk=pk)
        feedback.see += 1
        feedback.save()
        comments = CommentModel.objects.filter(feedback=feedback)
        print(comments)
        context = {
            'feedback': feedback,
            'comments': comments
        }
        return render(request, 'comments/comment.html', context)
    except FeedbackModel.DoesNotExist:
        return render(request, '404/404.html')

@login_required
def commentDetailView(request, pk, user_id):
    try:
        feedback = FeedbackModel.objects.get(pk=pk)