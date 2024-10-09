from django.contrib import admin
from comments.models import CommentModel


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'offer_title', 'author')

    def offer_title(self, obj):
        return obj.offer_id.title

    def author(self, obj):
        return obj.user_id

    offer_title.short_description = 'Offer Title'
    author.short_description = 'Author'
