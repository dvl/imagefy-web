# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='wish',
            options={'verbose_name_plural': 'Wishes'},
        ),
        migrations.AddField(
            model_name='offer',
            name='shopify_product_id',
            field=models.IntegerField(default=1234, verbose_name='Shopify Product ID'),
            preserve_default=False,
        ),
    ]