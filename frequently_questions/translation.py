from modeltranslation.translator import TranslationOptions, register

from frequently_questions.models import FrequentlyQuestionsModel


@register(FrequentlyQuestionsModel)
class FeedbackModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
