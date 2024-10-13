# forms.py
from django import forms

from .models import FeedbackModel


class FeedbackRequestForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['title', 'description', 'feedback_type']
