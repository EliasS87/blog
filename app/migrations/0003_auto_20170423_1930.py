# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170422_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
