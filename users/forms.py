from django import forms
from django.contrib.auth.hashers import make_password

from users.models import UserModel


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(validators='Password must be at least 8 characters long', widget=forms.PasswordInput,
                               min_length=8, label='Password')

    class Meta:
        model = UserModel
        fields = ['full_name', 'username', 'email', 'password']

    def save(self, commit=True):
        print(self.cleaned_data)
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.EmailField(max_length=255, label='Username')
    password = forms.CharField(max_length=255, label='Password')
