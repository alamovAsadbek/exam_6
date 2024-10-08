from modeltranslation.translator import TranslationOptions, register

from feedbacks.models import FeedbackModel


@register(FeedbackModel)
class FeedbackModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
