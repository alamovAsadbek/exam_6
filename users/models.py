from django.db import models
from django.utils.translation import gettext as _


class UserModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_('Full Name'))
    linkedin_url = models.URLField(max_length=200, verbose_name=_('LinkedIn URL'))
    email = models.EmailField(max_length=100, verbose_name=_('Email'))
    image = models.ImageField(upload_to='team_avatars/', verbose_name=_('Profile Image'))
    password = models.CharField(max_length=100, verbose_name=_('Password'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
