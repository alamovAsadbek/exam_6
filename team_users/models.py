from django.db import models
from django.utils.translation import gettext as _


class TeamUserModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last Name'))
    image = models.ImageField(upload_to='team_users/images/', verbose_name=_('Image'))
    role = models.CharField(max_length=100, verbose_name=_('Role'))
    description = models.TextField(verbose_name=_('Description'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Team User')
        verbose_name_plural = _('Team Users')

    def __str__(self):
        return self.first_name + " " + self.last_name
