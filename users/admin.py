from django.contrib import admin
from .models import ProfileModel


@admin.register(ProfileModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__first_name', 'user__last_name', 'user__username',)
    list_display_links = ('id', 'user__first_name', 'user__last_name', 'user__username',)
    search_fields = ('user__first_name', 'user__last_name', 'user__username',)
