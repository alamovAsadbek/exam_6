from django.shortcuts import render, redirect

from comments.models import CommentModel
from feedbacks.models import FeedbackModel
from .forms import CommentForm


def createCommentView(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.feedback = FeedbackModel.objects.get(pk=pk)
            comment.save()
            return redirect('create_comment', pk=pk)
    elif request.method == 'GET':
        feedback = FeedbackModel.objects.get(pk=pk)
        feedback.see += 1
        feedback.save()
        comments = CommentModel.objects.filter(feedback=feedback)
        context = {
            'feedback': feedback,
            'comments': comments
        }
        return render(request, 'comments/comment.html', context)
    else:
        return render(request, '404/404.html')
