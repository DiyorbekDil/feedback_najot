from django.db import models
from users.models import Common


class TeamModel(Common):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    experience_description = models.TextField()
    position = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class FAQModel(Common):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
