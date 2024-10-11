from django.db import models


class LikeModel(models.Model):
    user = models.ForeignKey('users.UserModel', on_delete=models.CASCADE, null=True, blank=True, related_name='likes')
    post = models.ForeignKey('feedbacks.FeedbackModel', on_delete=models.CASCADE, null=True, blank=True,
                             related_name='post_likes')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
