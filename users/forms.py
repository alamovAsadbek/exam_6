from django import forms

from users.models import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['full_name', 'email', 'password']
