from modeltranslation.translator import TranslationOptions, register

from .models import UserModel


@register(UserModel)
class FeedbackModelTranslationOptions(TranslationOptions):
    fields = ('full_name')
