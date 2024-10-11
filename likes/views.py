from likes.models import LikeModel


def like_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        user_id = request.POST.get('user_id')  # Agar foydalanuvchi identifikatori kerak bo'lsa

        # Yangi like qo'shish
        LikeModel.objects.create(post=post_id, user=user_id*1)
