# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20180706_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
