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
