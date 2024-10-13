from django import forms

from users.models import UserModel


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class UserLoginForm(forms.Form):
    username = forms.EmailField(max_length=255, label='Username')
    password = forms.CharField(max_length=255, label='Password')
