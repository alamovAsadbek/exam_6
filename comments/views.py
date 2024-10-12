from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from comments.models import CommentModel
from feedbacks.models import FeedbackModel
from .forms import CommentForm


@login_required
def createCommentView(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            form.cleaned_data['user'] = request.user
            comment.user = request.user
            print(form.cleaned_data)
            form.save()
            return redirect('create_comment', pk=pk)
    elif request.method == 'GET':
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
    return render(request, '404/404.html')
