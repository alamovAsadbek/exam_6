from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import FeedbackModel


@admin.register(FeedbackModel)
class FeedbackModelAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description', 'status', 'created_at', 'updated_at')
