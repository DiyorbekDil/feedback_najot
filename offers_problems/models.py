from django.db import models
from users.models import Common
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class OfferModel(Common):
    title = models.CharField(max_length=128, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    user_id = models.ForeignKey(User, related_name='offer', on_delete=models.SET_NULL, null=True,
                                verbose_name=_('User'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')


class ProblemModel(Common):
    title = models.CharField(max_length=128, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Problem')
        verbose_name_plural = _('Problems')
