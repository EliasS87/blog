# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170423_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_blurb',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
