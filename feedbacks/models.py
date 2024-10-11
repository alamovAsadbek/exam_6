from django.db import models

from django.utils.translation import gettext as _


class FeedbackModel(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    status = models.BooleanField(default=True, verbose_name=_('Status'))
    user = models.ForeignKey('users.UserModel', on_delete=models.CASCADE, null=True, verbose_name=_('User'))
    see = models.IntegerField(default=0, verbose_name=_('See'))

    choices = (
        ('offer', 'Offer'),
        ('problem', 'Problem')
    )
    feedback_type = models.CharField(max_length=20, choices=choices, verbose_name=_('Feedback Type'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Feedbacks')
        verbose_name = _('Feedback')
