from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserModel(AbstractUser):
    full_name = models.CharField(max_length=100, verbose_name=_('Full Name'))
    linkedin_url = models.URLField(max_length=200, verbose_name=_('LinkedIn URL'), null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name=_('Email'), unique=True)
    is_active = models.BooleanField(default=False, verbose_name=_('Status'))
    image = models.ImageField(upload_to='team_avatars/', verbose_name=_('Profile Image'), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    USERNAME_FIELD = 'email'  # Email ni asosiy identifikator sifatida belgilaymiz
    REQUIRED_FIELDS = ['full_name']  # Ro'yxatdan o'tishda talab qilinadigan maydonlar

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # O'zgartiring
        blank=True,
        help_text=_('Guruhlar.'),
        verbose_name=_('Guruhlar')
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # O'zgartiring
        blank=True,
        help_text=_('Foydalanuvchilarga berilgan ruxsatlar.'),
        verbose_name=_('Ruxsatlar')
    )

    def set_password(self, raw_password):
        super().set_password(raw_password)  # Django'ning ichki mexanizmini ishlatish

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
