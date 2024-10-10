from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from users.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(TranslationAdmin):
    list_display = ('id', 'full_name', 'email', 'is_active',)
    list_display_links = ('id', 'full_name', 'email', 'is_active',)
