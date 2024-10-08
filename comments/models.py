from django.db import models
from django.utils.translation import gettext as _


class CommentModel(models.Model):
    text = models.TextField(verbose_name=_('Comment'))
    user = models.ForeignKey('users.UserModel', on_delete=models.CASCADE, verbose_name=_('User'))
    feedback = models.ForeignKey('feedbacks.FeedbackModel', on_delete=models.CASCADE, verbose_name=_('Feedback'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.text
