# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomination', '0004_auto_20170406_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
