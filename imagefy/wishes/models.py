from django.conf import settings
from django.db import models

from taggit.managers import TaggableManager

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    parent = TreeForeignKey(
        to='self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
    )

    name = models.CharField(
        verbose_name='Name',
        max_length=50,
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{}'.format(self.name)


class Wish(models.Model):
    category = models.ForeignKey(
        to='Category',
    )

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
