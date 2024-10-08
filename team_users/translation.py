from modeltranslation.translator import TranslationOptions, register

from team_users.models import TeamUserModel


@register(TeamUserModel)
class FeedbackModelTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'role', 'description')
