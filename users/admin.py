from django.contrib import admin
from users.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
