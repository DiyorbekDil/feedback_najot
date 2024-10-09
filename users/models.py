from django.db import models


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserModel(Common):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

