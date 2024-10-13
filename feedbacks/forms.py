# forms.py
from django import forms

from .models import FeedbackModel


class FeedbackProblemForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['title', 'description', 'feedback_type']


class FeedbackOfferForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['title', 'description', 'feedback_type']
