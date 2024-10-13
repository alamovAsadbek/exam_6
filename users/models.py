from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


# validation image for user registration form
def validate_image_size(image):
    max_size = 5 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError("The maximum file size that can be uploaded is 5MB.")


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Profile"), related_name='profile')
    organization_name = models.CharField(verbose_name=_("Organization Name"), max_length=64, null=True, blank=True)
    location = models.CharField(verbose_name=_("Location"), max_length=64, null=True, blank=True)
    linkedin_link = models.CharField(verbose_name=_("Linkedin"), max_length=64, null=True, blank=True)
    avatar = models.ImageField(verbose_name=_("Avatar"), upload_to="users/", default='files/default_avatar.jpeg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
