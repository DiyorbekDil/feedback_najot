from django.db import models
from users.models import Common, UserModel


class OfferModel(Common):
    title = models.CharField(max_length=128)
    description = models.TextField()
    user_id = models.ForeignKey(UserModel, related_name='offer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'


class ProblemModel(Common):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Problem'
        verbose_name_plural = 'Problems'
