from django import forms
from django.core.exceptions import ValidationError

from users.models import UserModel


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['full_name', 'username', 'password']


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=255, label='Email')
    password = forms.CharField(max_length=255, label='Password')


# validation image for user registration form
def validate_image_size(image):
    max_size = 5 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError("The maximum file size that can be uploaded is 5MB.")
