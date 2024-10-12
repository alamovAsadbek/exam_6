from django.contrib import admin

from .models import TeamUserModel


@admin.register(TeamUserModel)
class TeamUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'role', 'description', 'created_at', 'updated_at')
