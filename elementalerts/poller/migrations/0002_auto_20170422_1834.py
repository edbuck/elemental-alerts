# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='last_sample_epoch',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='machine',
            name='last_sample_temp',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
    ]
