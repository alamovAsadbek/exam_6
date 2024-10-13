from django.contrib.auth.models import User
from django.db import models


class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='likes')
    post = models.ForeignKey('feedbacks.FeedbackModel', on_delete=models.CASCADE, null=True, blank=True,
                             related_name='post_likes')
    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return f"{self.user} liked {self.post}"
