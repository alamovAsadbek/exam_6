from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class UserModel(AbstractBaseUser):
    full_name = models.CharField(max_length=100, verbose_name=_('Full Name'))
    linkedin_url = models.URLField(max_length=200, verbose_name=_('LinkedIn URL'), null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name=_('Email'), unique=True)
    is_active = models.BooleanField(default=False, verbose_name=_('Status'))
    image = models.ImageField(upload_to='team_avatars/', verbose_name=_('Profile Image'), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    USERNAME_FIELD = 'email'  # Email ni asosiy identifikator sifatida belgilaymiz
    REQUIRED_FIELDS = ['full_name']  # Ro'yxatdan o'tishda talab qilinadigan maydonlar

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
