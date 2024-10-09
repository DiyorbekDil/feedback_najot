from django.contrib import admin
from offers_problems.models import *


@admin.register(OfferModel)
class OfferModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')

    def author(self, obj):
        return obj.user_id

    author.short_description = 'Author'


@admin.register(ProblemModel)
class ProblemModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
