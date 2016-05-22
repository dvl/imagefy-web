from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


class Profile(models.Model):
    SALESMAN = 'salesman'
    CUSTOMER = 'customer'

    TYPE_CHOICES = (
        (SALESMAN, 'Salesman'),
        (CUSTOMER, 'Customer')
    )

    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
    )

    type = models.CharField(
        max_length=9,
        choices=TYPE_CHOICES,
    )

    def get_avatar_url(self):
        try:
            return self.user.socialaccount_set.all()[0].get_avatar_url()
        except IndexError:
            return None


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        try:
            Token.objects.create(user=instance)
        except:
            pass  # yeah I know...
