from django.shortcuts import render

from comments.models import CommentModel
from feedbacks.models import FeedbackModel


def createCommentView(request, pk):
    feedback = FeedbackModel.objects.get(pk=pk)
    feedback.see += 1
    feedback.save()
    comments = CommentModel.objects.filter(feedback=feedback)
    context = {
        'feedback': feedback,
        'comments': comments
    }
    return render(request, 'comments/comment.html', context)
