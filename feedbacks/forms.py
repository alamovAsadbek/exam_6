# forms.py
from django import forms

from .models import FeedbackModel


class FeedbackProblemForm(forms.ModelForm):
    print("Problem form")

    class Meta:
        model = FeedbackModel
        fields = ['title', 'description', 'feedback_type']


class FeedbackOfferForm(forms.ModelForm):
    print("Offer form")

    class Meta:
        model = FeedbackModel
        fields = ['title', 'description', 'feedback_type', 'user']
