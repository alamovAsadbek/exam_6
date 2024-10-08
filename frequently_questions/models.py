from django.db import models
from django.utils.translation import gettext as _


class FrequentlyQuestionsModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Frequently Questions')
        verbose_name_plural = _('Frequently Questions')
