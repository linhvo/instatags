# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_tag_media_location_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='url',
            field=models.CharField(max_length=1000),
        ),
    ]