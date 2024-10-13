from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


# validation image for user registration form
def validate_image_size(image):
    max_size = 5 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError("The maximum file size that can be uploaded is 5MB.")


class UserModelManager(BaseUserManager):
    def create_user(self, email, username, full_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, username, full_name, password, **extra_fields)


class UserModel(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, verbose_name=_('Full Name'))
    linkedin_url = models.URLField(max_length=200, verbose_name=_('LinkedIn URL'), null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name=_('Email'), unique=True)
    is_active = models.BooleanField(default=False, verbose_name=_('Status'))
    username = models.CharField(max_length=100, verbose_name=_('Username'), unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    objects = UserModelManager()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
