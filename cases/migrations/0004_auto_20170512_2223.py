# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 19:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_auto_20170512_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2017, 5, 12, 22, 23, 3, 394000)),
        ),
    ]
