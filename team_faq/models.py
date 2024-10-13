from django.db import models
from users.models import Common
from django.utils.translation import gettext_lazy as _


class TeamModel(Common):
    first_name = models.CharField(max_length=64, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=64, verbose_name=_('Last name'))
    experience_description = models.TextField(verbose_name=_('Experience description'))
    position = models.CharField(max_length=64, verbose_name=_('position'))
    avatar = models.ImageField(upload_to='media', null=True, blank=True, verbose_name=_('Avatar'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')


class FAQModel(Common):
    question = models.TextField(verbose_name=_('Question'))
    answer = models.TextField(verbose_name=_('Answer'))

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')
