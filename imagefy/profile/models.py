from django.db import models
from django.conf import settings


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

    def get_account_type(self):
        return self.SALESMAN  # FIX-ME!!11
