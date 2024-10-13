from modeltranslation.translator import TranslationOptions, register

from .models import UserModel


@register(UserModel)
class FeedbackModelTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')
