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


class UserModel(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last Name'))
    linkedin_url = models.URLField(max_length=200, verbose_name=_('LinkedIn URL'), null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name=_('Email'), unique=True)
    password = models.CharField(max_length=100, verbose_name=_('Password'))
    username = models.CharField(max_length=100, verbose_name=_('Username'), unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
