# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-13 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_itemlost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlost',
            name='Returned',
            field=models.BooleanField(default=False),
        ),
    ]
