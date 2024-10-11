from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from team_users.models import TeamUserModel


@admin.register(TeamUserModel)
class TeamUserAdmin(TranslationAdmin):
    list_display = ('id', 'first_name', 'last_name', 'role', 'description', 'created_at', 'updated_at')
