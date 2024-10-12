from django import forms

from users.models import UserModel


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['full_name', 'username', 'password']


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=255, label='Email')
    password = forms.CharField(max_length=255, label='Password')
