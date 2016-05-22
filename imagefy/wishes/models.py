from django.conf import settings
from django.db import models

from taggit.managers import TaggableManager


class Wish(models.Model):
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
    )

    photo = models.ImageField(
        verbose_name='Photo',
    )

    detail = models.TextField(
        verbose_name='Detail',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    tags = TaggableManager()

    class Meta:
        verbose_name_plural = 'Wishes'


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
