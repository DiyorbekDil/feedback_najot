from django.db import models
from django.contrib.auth.hashers import make_password


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserModel(Common):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='user_avatar', null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

