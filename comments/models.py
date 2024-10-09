from django.db import models
from users.models import Common, UserModel
from offers_problems.models import OfferModel


class CommentModel(Common):
    content = models.TextField()

    offer_id = models.ForeignKey(OfferModel, related_name='comment', on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
