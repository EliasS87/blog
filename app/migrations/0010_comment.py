# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-05 17:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20170922_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField(max_length=1000)),
                ('pub_date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
