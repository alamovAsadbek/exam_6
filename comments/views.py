from django.shortcuts import render


def createCommentView(request):
    return render(request, 'comments/comment.html')
