from django import forms

from users.models import UserModel


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['full_name', 'email', 'password']


class UserLoginForm(forms.Form):
    pass
