from django.contrib import admin
from Team_FAQ.models import *


@admin.register(TeamModel)
class TeamModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'position')


@admin.register(FAQModel)
class FAQModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')