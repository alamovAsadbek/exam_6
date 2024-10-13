from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import UserModel


@admin.register(UserModel)
class UserModelAdmin(TranslationAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username',)
    list_display_links = ('id', 'first_name', 'last_name', 'username',)
    search_fields = ('first_name', 'last_name', 'username',)
