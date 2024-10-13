from django.db import models
from users.models import Common
from django.contrib.auth.models import User
from offers_problems.models import OfferModel
from django.utils.translation import gettext_lazy as _


class CommentModel(Common):
    content = models.TextField(verbose_name=_('Content'))

    offer_id = models.ForeignKey(OfferModel, related_name='comment', on_delete=models.CASCADE,
                                 verbose_name=_('Offer'))
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment', verbose_name=_('User'))

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
