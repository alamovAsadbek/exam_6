from django import forms
from django.contrib.auth import authenticate

from users.models import UserModel


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['full_name', 'email', 'password']


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=255, label='Email')
    password = forms.CharField(max_length=255, label='Password', widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise forms.ValidationError("Email yoki parol noto'g'ri")
        return self.cleaned_data
