# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 17:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('wishes', '0001_initial'), ('wishes', '0002_wish_buget'), ('wishes', '0003_remove_wish_tags')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopify_product_id', models.IntegerField(verbose_name='Shopify Product ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('salesman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Photo')),
                ('brief', models.CharField(max_length=140, verbose_name='Brief')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('buget', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Budget')),
            ],
            options={
                'verbose_name_plural': 'Wishes',
            },
        ),
        migrations.AddField(
            model_name='offer',
            name='wish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='wishes.Wish'),
        ),
    ]