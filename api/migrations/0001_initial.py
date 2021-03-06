# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-11 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_id', models.IntegerField()),
            ],
        ),
    ]
