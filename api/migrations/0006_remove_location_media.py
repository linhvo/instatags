# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 03:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_change_url_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='media',
        ),
    ]
