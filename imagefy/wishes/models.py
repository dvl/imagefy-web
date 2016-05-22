from django.conf import settings
from django.db import models


class Wish(models.Model):
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
    )

    photo = models.ImageField(
        verbose_name='Photo',
    )

    brief = models.CharField(
        verbose_name='Brief',
        max_length=140,
        blank=True,
        null=True,
    )

    buget = models.DecimalField(
        verbose_name='Budget',
        max_digits=8,
        decimal_places=2,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name_plural = 'Wishes'

    def __str__(self):
        return '{}'.format(self.brief)

    @property
    def budget(self):
        return self.buget


class Offer(models.Model):
    wish = models.ForeignKey(
        to='wish',
        related_name='offers',
    )

    salesman = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
    )

    shopify_product_id = models.IntegerField(
        verbose_name='Shopify Product ID'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return '{}'.format(self.shopify_product_id)
