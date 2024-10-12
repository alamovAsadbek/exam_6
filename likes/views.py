from django.http import JsonResponse
from django.views import View

from .models import LikeModel


class LikeView(View):
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        user_id = request.POST.get('user_id')

        # Yangi "like" yaratish
        like, created = LikeModel.objects.get_or_create(post_id=post_id, user_id=user_id)

        return JsonResponse({'success': True, 'new_like_count': like.count})


class UnlikeView(View):
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        user_id = request.POST.get('user_id')

        # "Like"ni o'chirish
        LikeModel.objects.filter(post_id=post_id, user_id=user_id).delete()

        return JsonResponse({'success': True})
