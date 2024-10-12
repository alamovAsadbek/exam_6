from django.contrib import admin
from django.db import models

from .models import TeamUserModel


@admin.register(TeamUserModel)
class TeamUserAdmin(models.Model):
    list_display = ('id', 'first_name', 'last_name', 'role', 'description', 'created_at', 'updated_at')
