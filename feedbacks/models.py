from django.db import models

from django.utils.translation import gettext as _


class FeedbackModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20)
    user = models.ForeignKey('UserModel', on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)
    see = models.IntegerField(default=0)

    choices = (
        ('offer', 'Offer'),
        ('problem', 'Problem')
    )
    feedback_type = models.CharField(max_length=20, choices=choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Feedbacks')
        verbose_name = _('Feedback')
